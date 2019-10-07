from flask import Flask
from flask import redirect
from flask import url_for

app = Flask(__name__)


@app.route('/admin/')
def hello_admin():
    return 'Hello admin this is your site'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'hi {} how is this site '.format(guest)


@app.route('/user/<user>')
def hello_user(user):
    if user == "admin" or user == 'Admin':
        return  redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=user))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4321)
