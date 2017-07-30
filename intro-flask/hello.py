''' hello.py test flask application '''
from flask import Flask
from flask import render_template
# pylint: disable=invalid-name
app = Flask(__name__)


@app.route('/')
def index():
	''' serving default route / '''
	#return "<h1>Hello, world!</h1>"
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	''' serving route /user/<name> This route will return Hello <name>'''
	#return '<h1>Hello, {0}!</h1>'.format(name)
	return render_template('user.html', name=name)


if __name__ == '__main__':
	app.run(debug=True)
