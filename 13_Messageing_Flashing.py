from flask import Flask,render_template,flash,redirect,url_for,request

app = Flask(__name__)
app.secret_key = "!@#$%^&*"

@app.errorhandler(404)
def page_not_found(e):\
    return '<h1>Vatsal Page not Found</h1>'

@app.route('/')
def index():
    return render_template('Login_Page.html')

@app.route('/login', methods=["POST","GET"])
def login():
    error = None
    if request.method == "POST":
        if request.form["nm"] == "admin":
            # login successfully
            flash('{} were successfully logged in'.format(request.form["nm"]),"Success_categories")
            return redirect(url_for('success'))
        else:
            error = 'Invalid credentials'
    return render_template('login.html')

@app.route('/success_login')
def success():
    return render_template('success_page.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=1234)