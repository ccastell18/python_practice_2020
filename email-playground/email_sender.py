import smtplib
from email.message import EmailMessage


# email object
email = EmailMessage()
email["from"] = "Christopher Castellano"
email["to"] = "ccastell_1@hotmail.com"
email["subject"] = "You won 1,000,000 dollars!"

email.set_content("I am a Python Master")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    # starts server
    smtp.ehlo()
    # encryption
    smtp.starttls()
    # logs into server
    smtp.login("christopher.castellano1980@gmail.com", "Jimmyfarbez1")
    smtp.send_message(email)
    print("all good boss!")
