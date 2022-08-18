from flask import Flask, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return "File has been uploaded."
    return render_template('index.html', form=form)

@app.route('/file0/')
def file_download_zero():
    return send_file("Unit00.png", as_attachment=True)

@app.route('/file1/')
def file_download_one():
    return send_file("Unit01.png", as_attachment=True)

@app.route('/file2/')
def file_download_two():
    return send_file("Unit02.png", as_attachment=True)

@app.route('/file3/')
def file_download_three():
    return send_file("Unit03.png", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)