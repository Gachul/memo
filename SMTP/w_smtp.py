import smtplib
import os, copy
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

_RECIEVER = 'phy1280@entrolink.com'

with open('C:/Users/com/Desktop/Personal/resource/login.txt', 'r', encoding='utf-8') as f:
    datas = f.readlines()
    _EMAIL: str = datas[0].strip('\n')
    _PASSWORD: str = datas[1].strip('\n')
    
# 실행 확인
def practice() -> None:
    recv_domain = 'imap.gmail.com'
    recv_port = 993
    
    send_domain = 'smtp.gmail.com'
    send_port = 587 #TLS  |  SSL=465
    
    smtp = smtplib.SMTP_SSL(send_domain, 465)
    
    # smtp.ehlo()     # hello
    # smtp.starttls() # TLS 사용시 필요
    smtp.login(_EMAIL, _PASSWORD)
    
    msg = MIMEText('SMTP Test')
    msg['Subject'] = 'Title'
    # msg['To'] = _RECIEVER
    smtp.sendmail(_EMAIL, _RECIEVER, msg.as_string())
    
    smtp.quit()

class EmailHTMLContent:
    def __init__(self, str_subject, template, template_params):
        assert isinstance(template, Template)
        assert isinstance(template_params, dict)
        
        self.msg = MIMEMultipart()
        
        # Email Title
        self.msg['Subject'] = str_subject
        
        # Email Content
        str_msg = template.safe_substitute(**template_params)