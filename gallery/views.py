from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from django.views.generic import TemplateView, ListView ,DetailView
from .models import upload_photo
from .forms import GalleryCreateForm
# Create your views here.


def gallery_createview(request):
    form = GalleryCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        obj =upload_photo.objects.create(
                image_name = form.cleaned_data.get('image_name'),
                image	= form.cleaned_data.get('image'),

            )
        return HttpResponseRedirect("/gallery/")
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