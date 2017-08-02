from flask import Flask
from flask import render_template
from flask import session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret'

@app.route('/')
def index():
	if 'count' not in session:
		session['count'] = 1
	else:
		session['count'] += 1
	return render_template('index12.html', count=session['count'])

if __name__ == '__main__':
	app.run(debug=True)
