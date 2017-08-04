from django.shortcuts import render
from django.views import generic

from .models import Blat

class IndexView(generic.ListView):
	template_name = 'blat/home.html'
	context_object_name = 'blat_list'

	def get_queryset(self):
		return Blat.objects.order_by('-created_on')[:20]

class DetailView(generic.DetailView):
	model = Blat
	template_name = 'blat/detail.html'
	context_object_name = 'blat'