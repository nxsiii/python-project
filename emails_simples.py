import pandas as pd
import smtplib
from email.message import EmailMessage
import time

SMTP_SERVER = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 2525 # Port standard Mailtrap
USER_MAILTRAP = "9c9ab056b9bd91"
PASS_MAILTRAP = "9ba6cbebb60411"

try:
    df = pd.read_csv("input.csv")
except FileNotFoundError:
    print("Erreur : Crée d'abord le fichier 'contacts.csv' !")
    exit()

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.login(USER_MAILTRAP, PASS_MAILTRAP)
    print("Connexion réussie à Mailtrap !")

    for index, row in df.iterrows():

        print(f"Simulation envoyée à : {row['nom']} ({row['email']})")

        time.sleep(15)
       
        msg = EmailMessage()
        msg['Subject'] = "Prise de contact"
        msg['From'] = "ton-email@test.com" # Avec Mailtrap, tu peux mettre ce que tu veux
        msg['To'] = row['email']
        
        corps = f"Bonjour {row['nom']},\n\nJ'ai vu que tu travailles chez {row['entreprise']}. On se capte ?"
        msg.set_content(corps)

        smtp.send_message(msg)
     

print("\n--- Tous les emails sont dans ta boîte Mailtrap ! ---")
