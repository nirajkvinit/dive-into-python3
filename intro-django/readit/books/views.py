from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def list_books(request):
	return HttpResponse('Logged in user: ' + request.user.username)
