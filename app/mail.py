from threading import Thread
from flask import Flask, render_template
from flask_mail import Message
from app import app, mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject=subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()

def send_contact_me_email(name,email,message,phone):
    send_email('[ileri\'s portfolio page] Contact Me Message',
               sender=app.config['ADMIN_EMAIL'],
               recipients=app.config['CONTACT_ME_EMAIL'].split(),
               text_body=render_template('email/contact_me_email.txt',
                name=name,email=email,phone=phone,message=message),
               html_body=render_template('email/contact_me_email.html',
                name=name,email=email,phone=phone,message=message))
