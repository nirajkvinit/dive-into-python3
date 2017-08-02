from datetime import datetime
from flask import Flask
from flask import render_template
from flask import session
from flask import g

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret'

@app.before_request
def before_request():
	if not 'count' in session:
		session['count'] = 1
	else:
		session['count'] += 1
	g.when = datetime.now().strftime('%H:%M:%S')

@app.route('/')
def index():
	return render_template('index13.html', count=session['count'], when=g.when)

@app.route('/other')
def other():
	return render_template('other.html', count=session['count'], when=g.when)

if __name__ == '__main__':
	app.run(debug=True)
