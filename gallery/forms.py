from django import forms


class GalleryCreateForm(forms.Form):
	image_name	=forms.CharField(required=True)
	image		=forms.ImageField(required=True)

	def clean_name(self):
		image_name = self.cleaned_data.get("image_name")
		if image_name == "Hello":
			raise forms.ValidationError("Not a valid name")
		return image_name