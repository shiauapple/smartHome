import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#import serial
import time

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
    content = MIMEMultipart()
    content["subject"] = "[警報]"
    content["from"] = "s810648@email.nlhs.tyc.edu.tw"
    content["to"] = "shiauapple@outlook.com"
    content.attach(MIMEText("亂打"))

    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("s810648@email.nlhs.tyc.edu.tw", "abngkkhwscsnihwm")
        smtp.send_message(content)

        print("訊息已發送!")
    except Exception as e:
        print("Error message: ", e)