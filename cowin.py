from cowin_api import CoWinAPI
import datetime
import re
import smtplib
import time


date = datetime.datetime.today().strftime ('%d-%m-%Y')  # Optional. Takes today's date by default
min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit
slots = []


def fillslotsForGivenCenter(centers):
    for center in centers:
        sessions = center.get('sessions')
        for s in sessions:
            if( s.get('available_capacity') != 0 ) :
                slots.append(center.get('name'))



def sendMail():
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        # start TLS for security
        s.starttls()
  
        # Authentication
        s.login("senderEmailId", "senderEmailPassword")
  
        # message to be sent
        message = " ".join(slots)
        
  
        # sending the mail ( you can email to multiple people)
        s.sendmail("senderEmailId", ["receiverNo1EMailId", "receieveNo2MailId"], message)
        
  
        # terminating the session
        s.quit()
            
    

cowin = CoWinAPI()
while(1):
        #Get the disctrict Id using states.py, eg: chandigarh - 108
        #Chandigarh
        fillslotsForGivenCenter(cowin.get_availability_by_district('108', date, min_age_limit).get('centers'))
        #Mohali
        fillslotsForGivenCenter(cowin.get_availability_by_district('496', date, min_age_limit).get('centers'))

        now = datetime.datetime.now()

        print(slots)

        if slots:
                sendMail()
        else:
                print('email not sent')

        slots = []
        time.sleep(90)



