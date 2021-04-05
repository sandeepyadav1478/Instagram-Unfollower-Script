from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import NoSuchElementException 
from instagram_private_api import Client, ClientCompatPatch 
import time 
import os 

print("---------------------") 
#uname = "themayborn_" 
#pwd = "roomno108"
uname="24x71478@gmail.com"
pwd="qwer1478tyui"
count = 0
print("\nInitializing Process...")
options = Options() 
options.add_argument("--window-size=1366x720") 
options.add_argument("--incognito") 
chromedriver_path = 'C:/Users/sande/Downloads/chromedriver_win32/chromedriver.exe' 
print("\nProcess started.")
f = open("follow_req.txt","w") 
browser = webdriver.Chrome(executable_path=chromedriver_path, options=options) #Star Browser 
browser.get("https://www.instagram.com/") 
time.sleep(3) #Waiting 3 seconds after we open the page. 
#IG Login 
#login = browser.find_element_by_xpath ("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a") 
#login.click() 
#time.sleep (2) 
username=browser.find_element_by_name ("username") 
username.send_keys(uname) 
password =browser.find_element_by_name ("password") 
password.send_keys(pwd) 
login_button = browser.find_element_by_xpath ("//button[@type='submit']") 
login_button.click() 
time.sleep(6) 
browser.get("https://www.instagram.com/accounts/access_tool/current_follow_requests") 
while True: 
    try: 
        vm_button = browser.find_element_by_xpath ('//*[@id="react-root"]/section/main/div/article/main/button') 
        vm_button.click() 
        time.sleep(2)
        count+=1
        if count == 10:
            print("\n****Can't go further too many scripts, you to run script again after it completed.")
            break
    except NoSuchElementException: 
        break 
cfreq_source = browser.find_elements_by_xpath("//div[@class='-utLf']")  
for x in cfreq_source: 
 f.write(x.text+"\n") 
f.close()
print("\nGot the users you have sent follow request in \"follow_req.txt\" file, now exiting browser..." )
browser.quit() 

print("\nThe following are available users to unfollow:\n")
f=open("follow_req.txt","r")
print(f.read())
 
# Start deleting the follow requests 
api = Client(uname, pwd) 
f = open("follow_req.txt", "r").read().split("\n") 
for x in f: 
    if bool(x): 
        user_info = api.username_info(x) 
        uid = user_info['user']['pk'] 
        api.friendships_destroy(uid) 
        print("\nFollow request cancelled for: "+x)
