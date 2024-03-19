from flask import Flask 

app = Flask(__name__)

@app.route("/show/info")
def index():
	return "now you see me"

if __name__ == '__main__':
	app.run(host = '0.0.0.0',port = 9247)