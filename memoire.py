import pandas as pd
import time
from email.message import EmailMessage
import smtplib

df = pd.read_csv('input.csv')

SMTP_SERVER = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 2525 # Port standard Mailtrap
USER_MAILTRAP = "9c9ab056b9bd91"
PASS_MAILTRAP = "9ba6cbebb60411"


with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as smtp : 
    smtp.login(USER_MAILTRAP,PASS_MAILTRAP)
    
    for objet,ligne in df.iterrows():
        msg=EmailMessage()
        msg['To']= ligne['email']
        msg['From'] = 'ahaahah@.com'
        msg['Subject']= 'pc'

        corps = f'bjr c vous {ligne['nom']} ou pas '

        msg.set_content(corps)

        smtp.send_message(msg)

        time.sleep(15)