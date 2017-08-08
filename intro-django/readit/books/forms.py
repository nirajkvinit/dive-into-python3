from django import forms
from .models import Book

class ReviewForm(forms.Form):
	"""
	Form for reviewing a book
	"""

	is_favourite = forms.BooleanField(
		label = 'Favourite?',
		help_text = 'In your top 100 books of all time?',
		required = False,
	)

	review = forms.CharField(
		widget = forms.Textarea,
		min_length = 100,
		error_messages = {
			'required': 'Please enter your review',
			'min_length': 'Please write atleast 100 characters (You have written %(show_value)s',
		}
	)

class BookForm(forms.ModelForm)	:
	class Meta:
		model = Book
		fields = ['title', 'authors']