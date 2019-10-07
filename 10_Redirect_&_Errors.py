from flask import Flask, redirect, url_for, render_template, request, abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)  # 401 for unauthorized login
    else:
        return redirect(url_for('index'))


@app.route('/success')
def success():
    return 'logged in successfully'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
