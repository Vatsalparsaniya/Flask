from flask import Flask,render_template
from flask_mail import Mail
from flask_mail import Message
import smtplib

app = Flask(__name__)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=587,
	MAIL_USE_TLS=True,
	MAIL_USERNAME = 'dathnote.ryuk@gmail.com',
	MAIL_PASSWORD = 'Vatsal@1999'
	)
mail = Mail(app)

@app.route('/')
def index():
    try:
        msg = Message("Hello, this message is from Flask app.",sender="dathnote.ryuk@gmail.com",recipients=["vatsalparsaniya@gmail.com"])
        msg.body = "testing-1"
        msg.html = "<b>testing-2</b>"
        mail.send(msg)
        return 'Mail sent'
    except Exception as e:
        return '<h1>Error : {}</h1>'.format(str(e))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1234)