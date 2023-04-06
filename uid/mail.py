from flask import Flask,redirect,url_for,request,render_template,make_response,session,abort,flash
from flask import *  
from flask_mail import *
#print(__name__)
app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'  
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME'] = 'microwebflask@gmail.com'  
app.config['MAIL_PASSWORD'] = 'qdaochqxfqlmgvfu'  
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True  

mail = Mail(app)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")
    

@app.route("/upload",methods=["POST"])
def upload():
    name=request.form["name"]
    email=request.form["email"]
    msg=Message("ENQUIRES ",sender="microwebflask@gmail.com",recipients=[email])
    msg.body="Want to know more about JK Constructions?\n Office working hours: 10 a.m. to 8 p.m. everyday, Sunday holiday "
    mail.send(msg)
    return render_template("home.html")


if __name__=="__main__":
    app.run(debug=True,port=3000)