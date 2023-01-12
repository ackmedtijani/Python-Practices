from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)


Bootstrap(app)


@app.route('/<int:num>')
def index(num):
    return 'Hello World + %i' % num

@app.route('/flask/')
@app.route('/flask/<name>')
def flask(name =None):
    return render_template('index.html' , name=name)

@app.route('/<name>')
def home(name = None):
	return render_template('home.html')

    
if __name__ ==  "__main__":
    app.run(debug = True)
