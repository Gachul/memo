import smtplib
import os, copy
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# instead Final Variable
_RECIEVER = 'phy1280@entrolink.com'

RECV_DOMAIN = 'imap.gmail.com'
RECV_PORT = 993
    
SEND_DOMAIN = 'smtp.gmail.com'
SEND_PORT = 587 #TLS  |  SSL=465



with open('C:/Users/com/Desktop/Personal/resource/login.txt', 'r', encoding='utf-8') as f:
    datas = f.readlines()
    _EMAIL: str = datas[0].strip('\n')
    _PASSWORD: str = datas[1].strip('\n')
    
# 실행 확인
def practice() -> None:
    
    smtp = smtplib.SMTP_SSL(SEND_DOMAIN, 465)
    
    # smtp.ehlo()     # hello
    # smtp.starttls() # TLS 사용시 필요
    smtp.login(_EMAIL, _PASSWORD)
    
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
    
Other_SMTP()