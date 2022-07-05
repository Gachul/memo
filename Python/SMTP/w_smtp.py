import smtplib
import os, copy
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# instead Final Variable
_RECIEVER = 'user01@localhost'

RECV_DOMAIN = 'imap.gmail.com'
RECV_PORT = 993
    
SEND_DOMAIN = 'smtp.gmail.com'
SEND_PORT = 587 #TLS  |  SSL=465

# _EMAIL = "root@192.168.255.84"
# _PASSWORD = "dnflskfk"



with open('C:/Users/com/Desktop/Personal/resource/login.txt', 'r', encoding='utf-8') as f:
    datas = f.readlines()
    _EMAIL: str = datas[0].strip('\n')
    _PASSWORD: str = datas[1].strip('\n')
    
# 실행 확인
def practice() -> None:
    
    smtp = smtplib.SMTP("192.168.255.84", 25)
    
    smtp.ehlo()     # hello
    smtp.starttls() # TLS 사용시 필요
    
    # smtp.login(_EMAIL, _PASSWORD)
    
    msg = MIMEText('SMTP Test')
    msg['Subject'] = 'Title'
    # msg['To'] = _RECIEVER
    smtp.sendmail(_EMAIL, _RECIEVER, msg.as_string())
    
    smtp.quit()
    
def Other_SMTP() -> None:
    
    smtp = smtplib.SMTP(SEND_DOMAIN, SEND_PORT)
    
    smtp.ehlo()
    smtp.starttls()
    smtp.login(_EMAIL, _PASSWORD)
    
    msg = MIMEText('SMTP Test')
    msg['Subject'] = 'Test'
    msg ['To'] = _RECIEVER

    smtp.sendmail(_EMAIL, _RECIEVER, msg.as_string())
    
    smtp.quit()
    
practice()