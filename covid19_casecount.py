import requests 
from bs4 import BeautifulSoup
import schedule
import time
from twilio.rest import Client
def request_stuff():
    URL = "https://www.worldometers.info/coronavirus/"
    r = requests.get(URL) 
    covid19=[]
    account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    auth_token = 'your_auth_token' 
    client = Client(account_sid, auth_token)
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.find('div', attrs = {'class':'content-inner'})
    for row in table.findAll('div', attrs = {'class':'maincounter-number'}):
        covid19.append(row.get_text("|", strip=True))
    for j in range(0,3):
        if(j==0):
            print("Total Cases:",covid19[j])
        if(j==1):
            print("Deaths: ",covid19[j])
        if(j==2):
            print("Recovered: ",covid19[j])
    message = client.messages \
    .create(
         body='\nTotal Cases: '+covid19[0]+'\n'+' Deaths: '+covid19[1]+'\n'+'  Recovered:  '+covid19[2]+'\n',
         from_='+15017122661', #the phone number provided by twilio with your account
         to='+15558675310' #the mobile you need to send the SMS
     )

schedule.every(30).minutes.do(request_stuff)
while True:
    schedule.run_pending()
    time.sleep(1)

