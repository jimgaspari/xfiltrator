# Import statements
# What you want to import from Python libraries
import os
from  flask import Blueprint, Flask, flash, request, redirect, render_template, send_from_directory
from werkzeug.utils import secure_filename

# Variable Definitions 
UPLOAD_FOLDER = './uploads'
DOWNLOAD_FOLDER = './downloads'
ALLOWED_EXTENTION = {'txt', 'pdf', 'doc', 'docx', 'xls', 'xlsx', 'csv', 'pdf', 'conf'}
bp = Blueprint('xfiltrate', __name__, url_prefix='/')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

app.secret_key = print(os.urandom(24))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENTION

@bp.route('/', methods=['GET'])
def mainpage():
    return render_template('main_page.html')

@bp.route('/downloads/', methods=['GET'])
def downloads():
    files = os.listdir(DOWNLOAD_FOLDER)
    return render_template('downloads.html', files=files)

@bp.route('/downloads/<path:filename>', methods=['GET'])
def get_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)

@bp.route('/fileupload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url) + '\n'
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url) + '\n'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = True
            return render_template('fileupload.html', success=success)
            # return filename + ' Upload Successfully\n' + render_template('fileupload.html')
        else:
            return "Not a valid file\n" + render_template('fileupload.html') + '\n'
    return render_template('fileupload.html')

# TODO ADD SOME Safety to the filename
@bp.route('/text/', methods=['GET', 'POST'])
def upload_text():
    filename = request.form['filename']
    text = request.form['text']
    if filename and text == '':
        flash('No Data Input')
        return redirect(request.url)
    if filename and text:
        with open(os.path.join(app.config['UPLOAD_FOLDER'],filename), 'w') as txt_file:
            txt_file.writelines(text)
    return render_template('text_upload.html')


if __name__ == '__main__':
    app.run()
