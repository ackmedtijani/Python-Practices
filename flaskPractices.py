from flask import Flask

app = Flask(__name___)

@app.route('/')

def home():
	return "Website Content goes here"

if name == "__main__":
	app.run(debug = True)