from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.utils import secure_filename
import os

Upload_folder = 'D:/Programming/Flask_learn/Upload'

Allowed_Extensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['upload_folder'] = Upload_folder
app.secret_key = 'vatsalparsaniya'


def allowed_file(Filename):
    return '.' in Filename and Filename.rsplit('.', 1)[1].lower() in Allowed_Extensions


@app.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("there is not any file part")
            return redirect(request.url)
        file = request.files['file']

        if file.name == '':
            flash("No selected File123")
            return request.url
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['upload_folder'], filename))
            flash("Done")
            return redirect(url_for('upload_file'))
    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        '''


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1234)
