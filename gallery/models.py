from django.db import models

# Create your models here.
class upload_photo(models.Model):
	image_name	=models.CharField(max_length=120)
	image		=models.ImageField(upload_to = 'media/',null=False)
	timestamp	=models.DateTimeField(auto_now=False,auto_now_add=True)