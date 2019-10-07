from flask import Flask, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)
app.secret_key = "Vatsal Parsaniya"  # any secret key


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return "Login as " + username + "<br>" + \
               "<br><h1><a href = '/logout'>click hear to logout<h1> "
    return "you are not login <h1><a href='/login'>click hear to login</h1>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return render_template('index.html') + " <h1><a href='/logout'>clock hear to logout</h1>"
    return render_template('Login.html')


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1234, debug=True)
