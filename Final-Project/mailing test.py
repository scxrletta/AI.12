import smtplib
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# email access
with open('D:\Will\Lectures\Outside\AI Indonesia - Basic Python\AI.12\Final-Project\password.txt', 'r') as f:
    password = f.read()

with open('D:\Will\Lectures\Outside\AI Indonesia - Basic Python\AI.12\Final-Project\message.txt', 'r') as f:
    message = f.read()

# sender & receiver
snd = 'tacc1711@gmail.com'
rcv = 'wsiagian11@gmail.com'

# MIME setup
msg = MIMEMultipart()
msg['From'] = snd
msg['To'] = rcv
msg['Subject'] = 'Test Mail. Hello!'

msg.attach(MIMEText(message, 'plain'))

# SMTP Setup
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login('tacc1711@gmail.com', password)
    txt = msg.as_string()
    server.sendmail(snd, rcv, txt)
    server.quit()
    print("Email sent!")
except Exception as exception:
    print("Error!")
