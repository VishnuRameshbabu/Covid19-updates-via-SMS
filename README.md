# Covid19-updates-via-SMS
<br />
<p>This project is based on a web scraper that scraps the data regarding the covid-19 cases worldwide and sends it to your mobile via SMS every 30 minutes.(The time delay between each SMS can be changed)</p><br />

## Installation
Installation of the required libraries
```bash
pip install -r requirements.txt
```
## Setting up your Twilio Account
[SignUp your first twilio account](https://www.twilio.com/try-twilio)   

You will be provided with a dashboard.

Go to Settings and you will see your 'ACCOUNT SID' and 'AUTH TOKEN' under 'LIVE CREDENTIALS'. <br />
![Verified Number](https://github.com/VishnuRameshbabu/Covid19-updates-via-SMS/blob/master/images/img2.png)

Go to 'Products and Services' on the left dashboard.

Then go to 'Phone numbers' under Super Network in order to get the numbers verified that you need to send the SMS update.<br />
You need to manually verify the numbers you need by clicking the '+'.<br />
![Verified Number](https://github.com/VishnuRameshbabu/Covid19-updates-via-SMS/blob/master/images/img1.png)

## Setting up the Program
Add your Account SID and Auth Token
```python
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token' 
```
Then add the trial number created for your Account and your verified number
```python
from_='+15017122661' #YOUR TRIAL PHONE NUMBER
to=' ' #THE VERIFIED NUMBER THAT YOU NEED TO SEND THE SMS
```

## Usage
Run the project using 
```python
python covid19_casecount.py
```



## Editing the time delay between each SMS
If you feel like you need to reduce or increase the time delay,this is the format. 
 
```python
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

```



