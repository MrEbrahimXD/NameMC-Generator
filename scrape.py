from concurrent.futures import thread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from bs4 import BeautifulSoup
import time
import threading



words = []
print("""

  _   _                      __  __         _____                           _             
 | \ | |                    |  \/  |       / ____|                         | |            
 |  \| | __ _ _ __ ___   ___| \  / | ___  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | . ` |/ _` | '_ ` _ \ / _ \ |\/| |/ __| | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |\  | (_| | | | | | |  __/ |  | | (__  | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_| \_|\__,_|_| |_| |_|\___|_|  |_|\___|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                          
* --------------------------------------------------------------------------------------- *
  Created by : MrEbrahimXD > https://mrebrahimxd.com

  Warning : This is for educational purposes , I'm not responsible of misuse or damage caused by
  This program

  Twitter : https://twitter.com/MrEbrahim_XD

* --------------------------------------------------------------------------------------- *

""")



try:
  file_to_read = str(input("Enter the path for the wordlist : "))
  path_to_webdriver = str(input("Enter the path for webdriver : "))
  headless = str(input("Headless mode (true - false) not recommended :  "))
  wait_time = int(input("Wait time if found errors (in seconds) : "))
  target_file = str(input("Enter a name for the file saving the list : "))
except:
  print("\nTry again , you've entered invalid text. ")
  exit()
  

with open(file_to_read ,'r') as file:
    words = file.readlines()
    




options = Options()
options.add_argument("start-maximized")
if headless == "true" or headless == "True":
  options.add_argument("--headless")

options.add_argument('--disable-logging')
options.add_argument("--log-level=2")
# options.set_preference('javascript.enabled', False)
options.add_experimental_option(
  "prefs",
  {
    'profile.managed_default_content_settings.javascript':2
  }
)
# Chrome is controlled by automated test software
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
s = Service(path_to_webdriver)
driver = webdriver.Chrome(service=s, options=options)

# Selenium Stealth settings
stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )

def getUrl():
  while True:
    try: 
      for word in words:
          words.pop(0)
          a = open(f"./target_file" ,'a')
          driver.get(f"https://namemc.com/search?q={word}")
          
          soup = BeautifulSoup(driver.page_source,'lxml')
          
          status_div = soup.find("div" , {"id" : "status-bar" } )
          
          # status = status_div.find("div" , {"id" , ""})
          print(status_div.text.strip())
          a.write(f"{word} status is { '<<<< Available >>>>' if 'Available' in status_div else 'Not Available' }\n")
          a.close()
          
          if word == "zzz":
              driver.quit()
              break
    except:
      print("There is an error happened , Trying again in 15 (s)")
      driver.get("https://mrebrahimxd.com")
      time.sleep(wait_time)
    finally:
      print("Trying again ..")





t = threading.Thread(target=getUrl)

threads = []

t.start()

for _ in range(10):
  threads.append(t)
  t.join()
    
