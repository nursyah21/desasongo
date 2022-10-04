import supabase
import threading

VITE_SUPABASE_URL='https://wtdtmfajzokjvmuvgzjv.supabase.co'
VITE_SUPABASE_ANON_KEY='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind0ZHRtZmFqem9ranZtdXZnemp2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjM3ODMwODAsImV4cCI6MTk3OTM1OTA4MH0.AJminOnfba8cOlYtLTPYUT78Gc00zCoSpejhb52tck4'

client = supabase.create_client(VITE_SUPABASE_URL, VITE_SUPABASE_ANON_KEY)


# class stats:
#   def __init__(self):
#     pass

#   def run(self):
#     try:
#       res = client.table("hidroponik").select("*").execute()
#       print(res.data)
      
#     except:
#       print("error")

def test():
  return client.table("hidroponik").select("*").limit(1).execute()

try:
  res = test()
  if res is not None and res.data is not None:print(res.data)  
except:
  pass



# c = stats()

# threading.Thread(target=c.run).start()