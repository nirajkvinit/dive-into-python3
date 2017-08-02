from flask import Flask
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Required
from wtforms.validators import Length


app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret'
bootstrap = Bootstrap(app)

class NameForm(Form):
	name = StringField('What is your name?', validators=[Required(), Length(1, 16)])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('index9.html', form=form, name=name)

if __name__ == '__main__':
	app.run(debug=True)
