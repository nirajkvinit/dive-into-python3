from flask import Flask
from flask import render_template
from flask import request
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	if request.method == 'POST' and 'name' in request.form:
		name = request.form['name']
	return render_template('index8.html', name=name)

if __name__ == '__main__':
	app.run(debug=True)
