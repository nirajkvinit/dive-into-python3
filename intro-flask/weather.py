from flask import flask
from flask import render_template

# pylint: disable=invalid-name
app = Flask(__name__)


@app.route('/')
def index():
	months = ["January", "February", "March", "April", "May", "June", "July", 
				"August", "September", "October", "November", "December"]
	return render_template('weather.html', city='Portland, OR', months=months)

if __name__ == '__main__':
	app.run(debug=True)