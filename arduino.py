import serial
import time
import codecs
import threading
import os
import supabase
import subprocess
from datetime import datetime


TTYACM = subprocess.getstatusoutput('ls /dev/ttyACM*')

arduino = serial.Serial(port=TTYACM[1], baudrate=9600, timeout=.1)

VITE_SUPABASE_URL='https://wtdtmfajzokjvmuvgzjv.supabase.co'
VITE_SUPABASE_ANON_KEY='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind0ZHRtZmFqem9ranZtdXZnemp2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjM3ODMwODAsImV4cCI6MTk3OTM1OTA4MH0.AJminOnfba8cOlYtLTPYUT78Gc00zCoSpejhb52tck4'
TIMECHANGE = 7 # use time 24hours
client = supabase.create_client(VITE_SUPABASE_URL, VITE_SUPABASE_ANON_KEY)

# read 
class CheckStats:
  def __init__(self):
    self._running = True
    self.__count = 0
    self.__datenow = datetime.now().day - 1
    self.data = {
      "tangki1":0.0, #read float
      "tangki2":0.0, #read float
      "tangki3":0.0, #read float
      "ppm":10, #ppm target (1-1500)
      "tds":0.0,  #read float
      "pompa1":1,
      "pompa2":1,
      "pompa3":1,
      "pompa4":1,
      "auto":1,
      "time_auto": TIMECHANGE,
    }
      
  def terminate(self):
    self._running = False

  def run(self):
    self._running = True
    state = 0
    stopauto = 0
    while self._running:
      #time.sleep(2)
      try:
        io = codecs.decode(arduino.readline().strip())
      except:
        print("error get data from arduino")
        continue

      if io.strip() != "" and io[0:5] == "State":
        a=os.system('date')

        try:
          self.data['tangki1'] = float(io.split('||')[1].split('=')[1])
          self.data['tangki2'] = float(io.split('||')[2].split('=')[1])
          self.data['tangki3'] = float(io.split('||')[3].split('=')[1])
          self.data['tds'] = float(io.split('||')[4].split('=')[1]) # current ppm
          self.data['ppm'] = int(io.split('||')[5].split('=')[1]) # ppm target
          self.data['pompa1'] = 1 if io.split('||')[6].split('=')[1].strip() == 'on' else 0
          self.data['pompa2'] = 1 if io.split('||')[7].split('=')[1].strip() == 'on' else 0
          self.data['pompa3'] = 1 if io.split('||')[8].split('=')[1].strip() == 'on' else 0
          self.data['pompa4'] = 1 if io.split('||')[9].split('=')[1].strip() == 'on' else 0
          mode_auto = io.split('||')[10].split('=')[1].strip() == 'auto'
          self.data['auto'] = True if mode_auto else False
          

          # state
          show = io.replace('jarak1', 'j_air').replace('jarak2','j_nutrisi').replace('jarak3','j_mix').replace('pompa1','p_isi').replace('pompa2','p_kuras').replace('pompa3','p_nutrisi').replace('pompa4','p_hidroponik')
          if(mode_auto == False):
            state = 0
            stopauto = 0

          if(self.data['auto']):
            self.data['pompa4'] = False
            ppm = self.data['tds']
            ppmtarget = self.data['ppm']
            tangki = self.data['tangki3'] #real
            # tangki = self.data['tangki1'] #only testing

            if (state == 0):
              show = f"State = {state} || {show[13:]}"
              self.data['pompa1'] = True
              if(tangki < 15):
                self.data['pompa1'] = False
                state = 1

            elif (state == 1):
              show = f"State = {state} || {show[13:]}"
              self.data['pompa3'] = True
              if(ppm >= ppmtarget and tangki < 15):
                state = 2
                self.data['pompa3'] = False
            
            elif (state == 2):
              show = f"State = {state} || {show[13:]}"
              if(ppm < ppmtarget-100 and tangki > 15):
                self.data['pompa2'] = False
                stopauto += 1
                state = 0
                if(stopauto == 10): #out from mode auto
                  stopauto = 0
                  state = 0
                  self.data['pompa4'] = True
                  self.data['pompa2'] = False
                  self.data['auto'] = False
                  mode_auto = False
                  self.send_data2()
                  try:
                    client.table('hidroponik').update({'auto':False, 'pompa4': True, 'pompa2': False}).match({'id_hidroponik':1}).execute()
                  except:
                    print('error sync data')
                    
              elif ( (ppm > ppmtarget+100 or tangki < 15) and state == 2):
                self.data['pompa2'] = True
              
            self.send_data2()

          print(f"{show}\n")
        

          # check time to mode auto
          if datetime.now().hour == self.data['time_auto'] and datetime.now().day != self.__datenow:
            self.data['auto'] = True
            self.send_data2()
            
            try:
              client.table('hidroponik').update({'auto':True}).match({'id_hidroponik':1}).execute()
            except:
              print('error sync data')

            self.__datenow = datetime.now().day          

        except:
          print("error to get data")

        self.__count += 1

      if self.__count >= 1000:
        a = os.system("clear")
        self.__count = 0
    
  def send_data2(self):
    data1 = f"{self.data['pompa1']},{self.data['pompa2']},{self.data['pompa3']},{self.data['pompa4']},{self.data['auto']},{self.data['ppm']}"
    arduino.write(bytes(data1,'utf-8'))

  def send_data(self):
    while True:
      time.sleep(10)

      try:
        data = client.table('hidroponik').select('*').execute()
        data = data.data[0]

        data1 = f"{data['pompa1']},{data['pompa2']},{data['pompa3']},{data['pompa4']},{data['auto']},{data['ppm']}"
        arduino.write(bytes(data1,'utf-8'))
        
        if data['auto'] == False:
          self.data['pompa1'] = 1 if data['pompa1'] == True else 0
          self.data['pompa2'] = 1 if data['pompa2'] == True else 0
          self.data['pompa3'] = 1 if data['pompa3'] == True else 0
          self.data['pompa4'] = 1 if data['pompa4'] == True else 0
        
        self.data['auto'] = 1 if data['auto'] == True else 0
        self.data['ppm'] = int(data['ppm'])
        
        # update time auto
        self.data['time_auto'] = data['time_auto']

        client.table('hidroponik').update(self.data).match({'id_hidroponik':1}).execute()          

        a=os.system('date')
        print("\nsync data\n")
      except:
        print("\nupdate data error\n")
  

if __name__ == "__main__":
  c = CheckStats()

  threading.Thread(target=c.run).start()
  threading.Thread(target=c.send_data).start()
