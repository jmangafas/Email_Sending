import smtplib
from email.message import  EmailMessage

email = EmailMessage()
email['from'] = 'email_address@hotmail.com'
email['to'] = 'email_address@hotmail.com'
email['subject'] = 'Hi Jim from Python!'

email.set_content("hello from Jim's Pycharm")

with smtplib.SMTP(host='smtp.live.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email_address@hotmail.com', 'add_password')
    smtp.send_message(email)
    print('Email Sent')
