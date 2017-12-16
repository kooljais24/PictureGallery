from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
# Create your views here.
def home(request):
	return render(request,"base.html",{})	

def contact(request):
	return render(request,"contact.html",{})	

def about(request):
	return render(request,"about.html",{})

class ContactView(View):
	def get(self, request,*args,**kwargs):
		return render(request,"contact.html",{})

class ContactView(TemplateView):
	template_name='contact.html'

class HomeView(TemplateView):
	template_name='home.html'

class AboutView(TemplateView):
	template_name='about.html'