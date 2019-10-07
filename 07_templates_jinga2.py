from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<user>/<int:score>/')
def render(user, score):
    dicte = {'phy': 54, 'che': 60, 'maths': 70}
    return render_template('variable_in_jinga.html', name=user, marks=score, result=dicte)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)
