from email.message import EmailMessage
import ssl
import smtplib

email_sender = "" #your email
email_password = "password" #your App password

email_receiver = "kahil75345@buzblox.com"

subject = "Email sent by Python program"
body = "You received email from a Python program"

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
