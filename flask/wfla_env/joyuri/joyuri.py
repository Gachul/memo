from flask import Flask, render_template, request

app = Flask(__name__, static_folder = 'static')

@app.route("/category")
def category_announcement():
    return render_template("category.html")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/hello")
def hello():
	return render_template("hiding/hello.html", title = "Hello")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "11029", threaded=True)