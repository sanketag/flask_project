from flask import Flask,render_template,request
import pymysql as sql
from tw import two
from thr import three 
from fou import four

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/home/pro/")
def pro():
    return render_template("project.html")

@app.route("/home/pro1/")
def pro1():
    r2,model = two()
    data = {
        # 'model' : mod,
        'r2' : r2
    }
    return render_template("pro1.html",data=data)
    
@app.route("/home/pro2/")
def pro2():
    return render_template("pro2.html")    

@app.route("/home/pro3/")
def pro3():
    return render_template("pro3.html")



app.run(host="localhost",port=5000,debug=True)