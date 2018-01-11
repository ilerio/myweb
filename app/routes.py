import os

from flask import Flask, render_template, flash, redirect, request, url_for, send_file
from datetime import datetime
from app import app
from app.form import ContactMeForm
from app.mail import send_contact_me_email

@app.context_processor
def inject_year():
    return {'year': datetime.utcnow().year}

@app.route('/')
@app.route('/index')
def index():
    form = ContactMeForm()
    return render_template('index.html', form=form)

@app.route('/contact_me', methods=['POST'])
def contact_me():
    form = ContactMeForm()
    name = form.name.data
    email = form.email.data
    phone = form.phone.data
    message = form.message.data
    if form.validate_on_submit():
        send_contact_me_email(name,email,message,phone)
        flash('Message successfully sent! I will get back to you ASAP.','success')
        return redirect('/')
    flash('Opps! Somethings wrong.','danger')
    return render_template('index.html', form=form)

@app.route('/resume')
def resume():
    file_path = os.path.abspath('app/files/Ilerioluwa_Oyedele_Resume.pdf')
    return send_file(file_path, attachment_filename='Ilerioluwa_Oyedele_Resume.pdf')
