import smtplib
from email.message import EmailMessage
import os

password = "qgioomyonmeawjsf"
sender_email = "dmitry-chief@yandex.ru"
receiver_email = "dmitry-chief@mail.ru"
subject = 'Проверка связи'
body = 'Письмо из скрипта'

msg = EmailMessage()
msg.set_content(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

smtp_server = "smtp.yandex.ru"
smtp_port = 465  # SSL

try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=10) as server:
        server.login(sender_email, password)
        server.send_message(msg)
    print ('Sent email')

except Exception as e:
    print(f"Не удалось отправить письмо: {e}")
#smtp_server = "smtp.mail.ru.com"