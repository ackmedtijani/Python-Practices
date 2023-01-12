from flask import Flask , render_template , session , redirect , url_for , flash
from flask_wtf import Form
from wtforms import StringField , SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap

class NameForm(Form):
	name = StringField('Name' , validators = [Required()])
	submit = SubmitField('Submit' , validators = [Required()])

app = Flask(__name__)
Bootstrap(app)

app.config['BOOTSTRAP_SERVE_LOCALLY'] = True
app.config['SECRET_KEY'] = 'Tijani'

@app.route('/<name>')
def index(name):
	return render_template('index.html' , name = name)

@app.route('/form')
def form():
	form = NameForm()
	if form.validate_on_submit():
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
	return render_template('SignUp.html' , form = form , name = session.get('name'))


if __name__ == '__main__':
	app.run(debug = True)