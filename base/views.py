import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import time
import re
import os

from django.shortcuts import render
from bluckmail.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, 'home.html')

def mail(request):
    code = ""
    mails = []
    sender_mail1 = request.POST.get('sender_email')
    Password1 = request.POST.get('Password')
    Subject = request.POST.get('Subject')
    Message = request.POST.get('message')
    
    print(Subject)
    
    myfile = request.FILES['myfile']
    data = myfile.read().decode()

    sender_email = "haripriyamax1427@gmail.com"
    password = "tlsleabaxjjryjjw"
    message = MIMEMultipart("alternative")
    message["Subject"] = "Testing App"
    message["From"] = sender_email
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
    server.ehlo()
    try:
        code = "the given mail id is accepted"
        server.login(sender_mail1, Password1)
    except:
        code = "The Given UserName or Password is worng so we re nent the mail from another mail"
        server.login(sender_email, password)
        

    count = 0
    reader = csv.reader(data.splitlines())
    next(reader)    
    for email in reader:
        for check in email:
            pat = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
            obj = re.match(pat, check)
            if obj:
                mails.append([email[0],email[0].split('@')[0],'Valid Email'])
                print("Valid Email")
            else:
                print("Invalid")
        
        subject = Subject
        message = Message
        send_mail(subject, message, EMAIL_HOST_USER, email, fail_silently=False)

        count += 1
        print(str(count), " Sent to ", email)
        if count % 80 == 0:
            server.quit()
            print("Server cooldown for 100 seconds")
            time.sleep(2000)
            server.ehlo()
            server.login(sender_email, password)
    server.quit()
    return render(request, 'home.html',{'mail':mails,'code':code})
