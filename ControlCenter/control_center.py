import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import serial
import time

S = serial.Serial('com5', 9600, timeout=2)


def sendEmailAlert(msg):
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
        content = MIMEMultipart()
        content["subject"] = "Gawr Gura:A!!!!"
        content["from"] = "Gawr Gura"
        content["to"] = "s810638@email.nlhs.tyc.edu.tw"
        content.attach(MIMEText("AAAAAAAAAA!"))
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("s810648@email.nlhs.tyc.edu.tw", "abngkkhwscsnihwm")
            smtp.send_message(content)
            print("訊息已發送!")
        except Exception as e:
            print("Error message: ", e)

IntruderAlert = False
while True:
    data = S.readline().decode().rstrip()

    if data == "alert" and not IntruderAlert:
        IntruderAlert = True
        print("斷路！！！")
        sendEmailAlert("AAAAAAAAAA")
    elif data == "normal" and IntruderAlert:
        IntruderAlert = False
        print("斷路解除")
        sendEmailAlert("A")
    time.sleep(1)