from flask import Flask


app = Flask(__name__)

name = input("Enter your Name : ")


@app.route('/')
def hello_world():
    return 'Hello {} nice to meet you'.format(name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)

