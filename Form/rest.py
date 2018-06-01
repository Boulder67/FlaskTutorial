from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
import os


app = Flask(__name__,static_folder='static/images')


# UPLOAD_FOLDER = '/media/nic/OldLaptopC-Programming/Laptop/Web-Development/VueJS/Form/Form/images'
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
UPLOAD_FOLDER = os.path.join('static/images')
#UPLOAD_FOLDER = os.path.join('static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formcomplete.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
# Database creation Start #
class usersinfo(db.Model):

   # id = db.Column('user_id', db.Integer, primary_key = True)
   # firstname = db.Column(db.String(100), unique=True)
   # lastname = db.Column(db.String(100), unique=True)
   # email   = db.Column(db.String(100), unique=True)
   # password = db.Column(db.String(140), unique=True)
   # age = db.Column(db.Integer, unique=True)
   # message = db.Column(db.String(500), unique=True)
   # infoRequest = db.Column(db.String(50))
   # sex = db.Column(db.String(50))
   # priority = db.Column(db.String(50))
   # pict = db.Column(db.String(50))
   id = db.Column('user_id', db.Integer, primary_key = True)
   firstname = db.Column(db.String(100), unique=False)
   lastname = db.Column(db.String(100), unique=False)
   email   = db.Column(db.String(100), unique=False)
   password = db.Column(db.String(140), unique=False)
   age = db.Column(db.Integer, unique=False)
   message = db.Column(db.String(500), unique=False)
   infoRequest = db.Column(db.String(50))
   sex = db.Column(db.String(50))
   priority = db.Column(db.String(50))
   pict = db.Column(db.String(50))


@app.route('/CustomerPage')
def CustomerPage():
   return render_template('CustomerPage.html')

@app.route('/Customer',methods = ['POST', 'GET'])
def Customer():
   if request.method == 'POST':
      upload = request.files['pic']
      print ("Upload is: ",upload)
      print("{} is the file name".format(upload.filename))
      savefilename = upload.filename
      print ("File name  is: ",savefilename)
      destination = os.path.join(app.config['UPLOAD_FOLDER'],savefilename)
      print ("Destination is: ",destination)
      upload.save(destination)
      #destination2 = destination
      destination2 = os.path.basename(os.path.dirname(destination))+"/"+savefilename
      #print("This is head and Tail: "  + tail)
      print ("Thsi is an Image Destination: "+destination2)

      user = usersinfo(firstname=request.form['firstname'],lastname=request.form['lastname'],email=request.form['email'],password=request.form['password'],age=request.form['age'],message=request.form['message'],infoRequest=request.form['infoRequest'],sex=request.form['sex'],priority=request.form['priority'],pict=destination2)


      db.session.add(user)
      db.session.commit()
      Hello = render_template("show_all.html", image_name=savefilename,usersinfo = usersinfo.query.all())

      #return redirect(url_for('show_all',imagename= savefilename ))
      return Hello


   else:
      user = request.args.get('firstname')
      return ("Data was not updated")
@app.route('/')
def show_all():

   return render_template('show_all.html', usersinfo = usersinfo.query.all())
if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)

