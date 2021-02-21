from flask import flash, redirect, url_for, render_template
from SayHello import app, db
from SayHello.models import Message
from SayHello.forms import HelloForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    helloform = HelloForm()
    if helloform.validate_on_submit():
        name = helloform.name.data
        body = helloform.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', form=helloform, messages=messages)
