import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login(' m.venugopal417@gmail.com','ybbf hokc smtw pkrk')
    msg=EmailMessage()
    msg['From']='your email'
    msg['Subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()


