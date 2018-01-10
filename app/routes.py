from flask import Flask, render_template, flash, redirect, request, url_for
from datetime import datetime
from app import app
from app.form import ContactMeForm

@app.context_processor
def inject_now():
    return {'year': datetime.utcnow().year}

@app.route('/')
@app.route('/index')
def index():
    form = ContactMeForm()
    return render_template('index.html', form=form)

@app.route('/contact_me', methods=['POST'])
def contact_me():
    form = ContactMeForm()
    if form.validate_on_submit():
        flash('CM | name:{}, mail:{}, #:{}, msg:{}'.format(form.name.data,
            form.email.data, form.phone.data, form.message.data),'success')
        return redirect('/index')
    flash('Opps! Somethings wrong.','danger')
    return render_template('index.html', form=form)
