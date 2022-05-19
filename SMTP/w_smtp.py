import smtplib
import os, copy
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
    
def practice():
    recv_domain = 'imap.gmail.com'
    recv_port = 993
    
    send_domain = 'smtp.gmail.com'
    send_port = 465
    
    smtp = smtplib.SMTP(send_domain, send_port)
    
    smtp.ehlo()     # hello
    smtp.starttls() # TLS 사용시 필요
    smtp.login()
    
    
    return 0

class EmailHTMLContent:
    def __init__(self, str_subject, template, template_params):
        assert isinstance(template, Template)
        assert isinstance(template_params, dict)
        
        self.msg = MIMEMultipart()
        
        # Email Title
        self.msg['Subject'] = str_subject
        
        # Email Content
        str_msg = template.safe_substitute(**template_params)