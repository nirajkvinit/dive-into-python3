import os
import imghdr
from flask import Flask
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import FileField
from wtforms import SubmitField
from wtforms import ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret'
bootstrap = Bootstrap(app)

class UploadForm(Form):
	image_file = FileField('Image File')
	submit = SubmitField('Submit')

	def validate_image_file(self, field):
		print(field.data.filename[-4])
		if field.data.filename[-4:].lower() != '.jpg':
			raise ValidationError('Invalid File extension')
		if imghdr.what(field.data) != 'jpeg':
			raise ValidationError('Invalid image format')

@app.route('/', methods=['GET', 'POST'])
def index():
	image = None
	form = UploadForm()
	if form.validate_on_submit():
		image = 'uploads/' + form.image_file.data.filename
		form.image_file.data.save(os.path.join(app.static_folder, image))
	return render_template('index11.html', form=form, image=image)

if __name__ == '__main__':
	app.run(debug=True)
