from flask import Flask
from flask import render_template
from flask import make_response
from flask import jsonify
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index14.html')

@app.route('/text')
def text():
	return render_template('text.txt'), 200, {'Content-Type': 'text/plain'}

@app.route('/xml')
def xml():
	return '<h1>This is shown as <b>XML</b> in the browser</h1>', 200, {'Content-Type': 'application/xml'}

@app.route('/json')
def json():
	return jsonify({'first_name': 'John', 'last_name': 'Smith'})

@app.route('/redirect')
def redir():
	return redirect(url_for('text'))

@app.route('/cookie')
def cookie():
	resp = redirect(url_for('index'))
	resp.set_cookie('cookie', 'Hello! I am a cookie')
	return resp

@app.route('/error')
def error():
	return 'Bad request', 400

@app.route('/response')
def response():
	resp = make_response(render_template('text.txt'))
	resp.headers['Content-Type'] = 'text/plain'
	return resp

if __name__ == '__main__':
	app.run(debug=True)