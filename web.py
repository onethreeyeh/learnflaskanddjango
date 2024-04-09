from flask import Flask,render_template

app = Flask(__name__)

@app.route("/show")
def index():
	return render_template("index.html")

@app.route("/whoami")
def whoami():
	return render_template("whoami.html")

@app.route("/dailylog")
def dailylog():
	return render_template("dailylog.html")

if __name__ == '__main__':
	app.run()	