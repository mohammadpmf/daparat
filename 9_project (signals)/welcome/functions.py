import os
import smtplib, ssl

from dotenv import load_dotenv
import ghasedakpack

load_dotenv()


def send_sms():
    sms = ghasedakpack.Ghasedak(os.getenv("GHASEDAK_API_KEY"))
    message = 'این اس ام اس از پایتون ارسال شده است. لغو۱۱'
    my_number_1 = os.getenv("PHONE_NUMBER_1")
    line_number = os.getenv("LINE_NUMBER")
    answer = sms.send({'message': message, 'receptor' : my_number_1, 'linenumber': line_number})
    print(answer)


def send_email():
    sender_email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("APP_PASSWORD")
    receiver_email = ["shookooljooni254@gmail.com"]
    message = "Subject: خوش آمدگویی\nاز این که در سایت ما ثبت نام کردید ممنونیم.\nبا تشکر\nمحمد پورمحمدی فلاح".encode('utf-8')
    smtp_server = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print('Email Sent!!!')
