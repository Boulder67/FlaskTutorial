from flask import Flask, render_template, request, redirect,url_for
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_page():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      urlm= f.filename

      return redirect(url_for('upload_page',urlm=urlm))

if __name__ == '__main__':
   app.run(debug = True)
