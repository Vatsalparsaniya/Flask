from flask import Flask,render_template,url_for,flash,redirect,request

app = Flask(__name__)
app.secret_key = '!@#$%^&*'

@app.errorhandler(404)
def Page_not_found(e):
    return '<h1>Page Not Found Vatsal do Something</h1>'

@app.route('/')
def index():
    try:
        return '<form action = "/login" method = "POST"><p>Enter Name:</p><p><input type = "text" name = "nm" /></p><p><input type = "submit" value = "submit" /></p></form>'
    except Exception as e:
        return str(e)

@app.route('/login', methods=["POST","GET"])
def login():
    try:
        if request.method =='POST':
            return render_template('Welcome.html')
    except Exception as e:
        return render_template('500.html',error=e)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=1234)