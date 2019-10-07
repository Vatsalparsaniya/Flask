from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render():
    return render_template('first_simple.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4321)
