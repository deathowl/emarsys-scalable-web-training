from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
app = Flask(__name__, static_folder="uploads")


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join("uploads/" + secure_filename(f.filename)))
        return 'file uploaded successfully'
    else:
        return render_template('upload.html')



if __name__ == '__main__':
    app.run(debug=True)
