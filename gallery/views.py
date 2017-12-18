from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import upload_photo
# Create your views here.
def gallery_listview(request):
	template_name='gallery/gallery_list.html'
	queryset=upload_photo.objects.all()
	context={
		"object_list":queryset	
	}
	return render(request,template_name,context)



