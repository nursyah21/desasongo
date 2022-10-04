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
      "ppm":10,
      "tds":0.0,  #read float
      "pompa1":1,
      "pompa2":1,
      "pompa3":1,
      "pompa4":1,
      "auto":1
    }
      
  def terminate(self):
    self._running = False
  
  def ppmtarget(self):
    print("press q to back to menu")
    opt1=input("please input your output(1-1500):")
    pass

  def mode(self):
    print("press q to back to menu")
    pass
  
  def pompa(self, target:int):
    print("press q to back to menu")
    pass

  def run(self):
    self._running = True
    while self._running:
      time.sleep(1)

      io = codecs.decode(arduino.readline().strip())
      print("""
menu hidroponik arduino
1. edit ppm target,
2. edit mode
3. mengaktifkan atau menonaktifkan pompa1
4. mengaktifkan atau menonaktifkan pompa2
5. mengaktifkan atau menonaktifkan pompa3
6. mengaktifkan atau menonaktifkan pompa4
      """)
      try:
        opt=int(input("please input your choice (1-6): "))

        if(opt == 1): self.ppmtarget()
        elif(opt == 2): self.mode()
        elif(opt == 3): self.pompa(1)
        elif(opt == 4): self.pompa(2)
        elif(opt == 5): self.pompa(3)
        elif(opt == 6): self.pompa(4)
        else: print("please only enter number 1-6")

      except:
        print("please input only number")

        
        
     
  def send_data(self):
    while True:
      time.sleep(15)
      try:
        client.table('hidroponik').update(self.data).match({'id_hidroponik':1}).execute()
        a=os.system('date')
        print("upload data\n")
      except:
        print("update data error")


c = CheckStats()
threading.Thread(target=c.run, args=()).start()

# threading.Thread(target=c.send_data).start()


