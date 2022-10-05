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

class Menu:
  def __init__(self):
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

  def ppmtarget(self):
    print("press q to back to menu\n")
    try:
      opt1= input("please input your output(1-1500): ")
      if opt1 == "q":return
      
      opt1 = int(opt1)
      if opt1 < 1 or opt1 > 1500:return print("please input only(1-1500)"), self.ppmtarget()

      data = self.getdata()
      data['ppm'] = opt1
      
      data1 = f"{data['pompa1']},{data['pompa2']},{data['pompa3']},{data['pompa4']},{data['mode']},{data['ppm']}"

      arduino.write(bytes("asdasd",'utf-8'))
      
      print(f"update ppmtarget to {opt1} success\n")
          
    except:
      print("please input only number\n")
      self.ppmtarget()

  def mode(self):
    print("press q to back to menu\n")
    opt = input("please input (m) to manual or (a) to auto: ")
    
    if opt == "q":return
    if opt == "m" or opt == "a":
      data = self.getdata()
      data['mode'] = True if opt == "a" else False
      data1 = f"{data['pompa1']},{data['pompa2']},{data['pompa3']},{data['pompa4']},{data['mode']},{data['ppm']}"
      
      arduino.write(bytes(data1,'utf-8'))

      opt = "auto" if opt == "a" else "manual"
      print(f"update mode to {opt} success\n")

    else:
      return print("please input m or a\n"), self.mode()
  
  def pompa(self, target:int):
    print("press q to back to menu\n")
    opt = input(f"update pompa{target}, press (y) to on or (n) to off: ")
    if opt == "q":return

    if opt == "y" or opt == "n":
      data = self.getdata()

      data[f"pompa{target}"] = True if opt == "y" else False
      data1 = f"{data['pompa1']},{data['pompa2']},{data['pompa3']},{data['pompa4']},{data['mode']},{data['ppm']}"
      
      try:
        g = codecs.decode(arduino.readline().strip())
        print(g)
        
        arduino.write(bytes(data1,'utf-8'))
        time.sleep(1) # waiting after send data

        g = codecs.decode(arduino.readline().strip())
        print(g)

        opt = "on" if opt == "y" else "off"
        print(f"update pompa{target} to {opt} success\n")
        
        opt = 1 if opt == "on" else 0
        self.senddata({f"pompa{target}":opt})

      except:
        print("error write and read arduino")


    else:
      return print("please input y or n\n"), self.pompa()

  def getdata(self):
    io = codecs.decode(arduino.readline().strip())
    if io.strip() != "" and io.strip()[0:5] == "State":
      data = io.split("||")
      
      try:
        ppm = int(data[5].split("=")[1].strip())
        pompa1 = True if data[6].split("=")[1].strip() == 'on' else False
        pompa2 = True if data[7].split("=")[1].strip() == 'on' else False
        pompa3 = True if data[8].split("=")[1].strip() == 'on' else False
        pompa4 = True if data[9].split("=")[1].strip() == 'on' else False
        mode = True if data[10].split("=")[1].strip() == 'auto' else False
        
        return {"ppm": ppm, "pompa1":pompa1, "pompa2":pompa2, "pompa3":pompa3, "pompa4":pompa4, "mode":mode}
      except:
        print("error", len(data))

    return ""

  def senddata(self, data):
    try:
      client.table('hidroponik').update(data).match({'id_hidroponik':1}).execute()
      print("update data\n")

    except:
      print("update data error\n")

  def run(self):
    print("""
menu hidroponik arduino
1. edit ppm target
2. edit mode
3. mengaktifkan atau menonaktifkan pompa1
4. mengaktifkan atau menonaktifkan pompa2
5. mengaktifkan atau menonaktifkan pompa3
6. mengaktifkan atau menonaktifkan pompa4

press q to exit
      """ )
    try:
      opt = input("please input your choice (1-6): ")
      if opt == "q":return

      opt=int(opt)
      if(opt == 1): self.ppmtarget()
      elif(opt == 2): self.mode()
      elif(opt == 3): self.pompa(1)
      elif(opt == 4): self.pompa(2)
      elif(opt == 5): self.pompa(3)
      elif(opt == 6): self.pompa(4)
      else: return print("please only enter number 1-6"), self.run()
    except:
      return print("please input only number"), self.run()


# read 
class CheckStats:
  def __init__(self):
    self._running = True
    self.__count = 0
    self.__menu = False
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

  def menu(self):
    while True:
      opt=input("")
      if opt == "q" and self.__menu:
        self.__menu = False
      elif opt == "q":
        self.__menu = True
        Menu().run()
        self.__menu = False

  def run(self):
    self._running = True
    while self._running:
      time.sleep(2)
      if self.__menu:continue
      io = codecs.decode(arduino.readline().strip())

      if io.strip() != "" and io[0:5] == "State" or io == "update arduino":
        a=os.system('date')
        print(f"{io}\n")
        #print("press q to enter menu")

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
      time.sleep(10)
      
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
  #threading.Thread(target=c.menu).start()
