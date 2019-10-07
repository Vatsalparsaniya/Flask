from flask import Flask
from flask import redirect
from flask import url_for
from flask import  request
from flask import  render_template

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_world(name):
    return 'Hello {} How are you'.format(name)


@app.route('/')
def render():
    return render_template('Login_Page.html')


@app.route('/success/<name>')
def hello_success(name):
    return 'hello, {} you have successfully login into our system '.format(name)


@app.route('/login/', methods=['POST', 'GET'])
def hello_login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('hello_success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('hello_success', name=user))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4321)
