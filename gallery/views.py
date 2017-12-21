from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from django.views.generic import TemplateView, ListView ,DetailView,CreateView
from .models import upload_photo
from .forms import GalleryCreateForm,GalleryListCreateForm
# Create your views here.

@login_required()
def gallery_createview(request):
	form = GalleryListCreateForm(request.POST or None, request.FILES or None)
	errors = None
	if form.is_valid():
		if request.user.is_authenticated():
			instance=form.save(commit=False)
			instance.owner=request.user
			instance.save()
			return HttpResponseRedirect("/gallery/")
		else:
			return HttpResponseRedirect("/login/")    		
	if form.errors:
		errors = form.errors
           
	template_name = 'gallery/form.html'
	context = {"form": form, "errors": errors}
	return render(request, template_name, context)


def gallery_listview(request):
	template_name='gallery/gallery_list.html'
	queryset=upload_photo.objects.all()
	context={
		"object_list":queryset	
	}
	return render(request,template_name,context)


class GalleryListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = upload_photo.objects.filter(
                    Q(category__iexact=slug) |
                    Q(category__icontains=slug)
                )
        else:
            queryset = upload_photo.objects.all()
        return queryset



class GalleryDetailView(DetailView):
    queryset = upload_photo.objects.all()
    
    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id) # pk = rest_id
    #     return obj

class GalleryCreateView(LoginRequiredMixin,CreateView):
	form_class=GalleryListCreateForm
	login_url='/login/'
	template_name='gallery/form.html'
	success_url='/gallery/'

	def form_valid(self,form):
		instance=form.save(commit=False)
		instance.owner=self.request.user
		return super(GalleryCreateView,self).form_valid(form)