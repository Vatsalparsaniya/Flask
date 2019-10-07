from flask import Flask

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_world(name):
    return 'Hello {} How are you'.format(name)


@app.route('/bye/<name>')
def bye_world(name):
    return '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>{}</title></head>' \
           '<body><p> <b>{}</b> first html file for flask connect through render_templates</p>' \
           '</body></html>'.format(name, name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4321, debug=True)


# open the browser and enter URL 192.168.0.105:4321/hello/vatsal/.
# open the browser and enter URL 192.168.0.105:4321/bye/vatsal/.
