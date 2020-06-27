from flask_mail import Message
from website import mail


def send_contact_email(name, email, message):
    msg = Message('AMDUG Contact Form', sender='noreply10665@gmail.com', recipients=['awang.yz@gmail.com']) # cc=[email],
    msg.body = f'''Name: {name}
Email: {email}
Message: {message}
'''
    mail.send(msg)