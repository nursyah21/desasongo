import serial
import time
import codecs
import threading
import os
import supabase

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)

VITE_SUPABASE_URL='https://wtdtmfajzokjvmuvgzjv.supabase.co'
VITE_SUPABASE_ANON_KEY='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind0ZHRtZmFqem9ranZtdXZnemp2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjM3ODMwODAsImV4cCI6MTk3OTM1OTA4MH0.AJminOnfba8cOlYtLTPYUT78Gc00zCoSpejhb52tck4'

client = supabase.create_client(VITE_SUPABASE_URL, VITE_SUPABASE_ANON_KEY)


# read 
class CheckStats:
  def __init__(self):
    self._running = True
    self.__count = 0
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
      "auto":1
    }
      
  def terminate(self):
    self._running = False

  def run(self):
    self._running = True
    while self._running:
      time.sleep(2)
      io = codecs.decode(arduino.readline().strip())

      if io.strip() != "" and io[0:5] == "State":
        a=os.system('date')
        print(f"{io}\n")

        try:
          self.data['tangki1'] = float(io.split('||')[1].split('=')[1])
          self.data['tangki2'] = float(io.split('||')[2].split('=')[1])
          self.data['tangki3'] = float(io.split('||')[3].split('=')[1])
          self.data['tds'] = float(io.split('||')[4].split('=')[1].strip())
          self.data['ppm'] = int(io.split('||')[5].split('=').strip())
        except:
          print("")

        self.__count += 1

      if self.__count >= 1000:
        os.system("clear")
        self.__count = 0
    
  def send_data(self):
    while True:
      time.sleep(15)
      
      try:
        data = client.table('hidroponik').select('*').execute()
        data = data.data[0]
        
        data1 = f"{data['pompa1']},{data['pompa2']},{data['pompa3']},{data['pompa4']},{data['auto']},{data['ppm']}"
        arduino.write(bytes(data1,'utf-8'))
        
        self.data['pompa1'] = 1 if data['pompa1'] == True else 0
        self.data['pompa2'] = 1 if data['pompa2'] == True else 0
        self.data['pompa3'] = 1 if data['pompa3'] == True else 0
        self.data['pompa4'] = 1 if data['pompa4'] == True else 0
        self.data['auto'] = 1 if data['auto'] == True else 0
        self.data['ppm'] = int(data['ppm'])

        client.table('hidroponik').update(self.data).match({'id_hidroponik':1}).execute()

        a=os.system('date')
        print("\nsync data\n")
      except:
        print("\nupdate data error\n")

  



if __name__ == "__main__":
  c = CheckStats()

  threading.Thread(target=c.run).start()
  threading.Thread(target=c.send_data).start()
