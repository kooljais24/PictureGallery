from django import forms

from .models import upload_photo

class GalleryCreateForm(forms.Form):
	image_name	=forms.CharField(required=True)
	image		=forms.ImageField(required=True,widget=forms.ClearableFileInput(attrs={'multiple': True}))

	def clean_name(self):
		image_name = self.cleaned_data.get("image_name")
		if image_name == "Hello":
			raise forms.ValidationError("Not a valid name")
		return image_name


class GalleryListCreateForm(forms.ModelForm):
	class Meta:
		model=upload_photo
		fields=[
			'image_name',
			'image'
		]

	def clean_name(self):
		image_name = self.cleaned_data.get("image_name")
		if image_name == "Hello":
			raise forms.ValidationError("Not a valid name")
		return image_name
