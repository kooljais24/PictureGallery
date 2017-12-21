from django.conf import settings
from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
# Create your models here.

User = settings.AUTH_USER_MODEL

class upload_photo(models.Model):
	owner		=models.ForeignKey(User)
	image_name	=models.CharField(max_length=120)
	image		=models.ImageField(upload_to = 'media/',null=False)
	timestamp	=models.DateTimeField(auto_now=False,auto_now_add=True)
	slug            = models.SlugField(null=True, blank=True) 
	def __str__(self):
		return self.image_name

	@property
	def title(self):
		return self.image_name


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()

pre_save.connect(rl_pre_save_receiver, sender=upload_photo)

# post_save.connect(rl_post_save_receiver, sender=upload_photo)