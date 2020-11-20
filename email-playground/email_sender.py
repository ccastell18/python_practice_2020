import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Chris"
email["to"] = "ccastell_1@hotmail.com"
email["subject"] = "You won a million dollars!"

email.set_content("I am a Python master")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("c.castellano1980@gmail.com", "Jimmyfarbez1")
    smtp.send_message(email)
    print("all good boss")
