from flask import Flask

app = Flask(__name__)


@app.route('/flask')
def hello_flask():
    return 'Hello this is flask'


@app.route('/python/')
def hello_python():
    return 'Hello this is Python'


if __name__ == '__main__':
    print("lol")
    app.run(host='0.0.0.0', port=1234)


# using /python or /python/ returns the same output. However,
# in case of the first rule, /flask/ URL results in 404 Not Found page.
