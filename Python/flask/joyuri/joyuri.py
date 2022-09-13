from flask import Flask, render_template, request
import external.user_info as uinfo
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder = 'static')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/category")
def category_announcement():
    return render_template("category.html")

@app.route("/hello")
def hello():
	return render_template("hiding/hello.html", title = "Hello")

@app.route("/izone")
def introduce_izone():
    return render_template("hiding/izone.html", title = "IZ*ONE")

@app.route("/upload")
def render_file():
    return render_template("hiding/upload_file.html")

@app.route("/fileUpload", methods = ["POST"])
def upload_file():
    if(request.method == "POST"):
        f = request.files['file']
        f.save("D:/Flask_saver/" + secure_filename(f.filename))
    return "Upload 완료"

@app.route("/login", methods = ["GET", "POST"])
def user_login():
    
    if request.method == "POST":
        result = request.form
        
        return render_template("home.html", title = "Home")
    
    return render_template("login.html", title = "Login")
    
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "11029", debug = True, threaded=True)
