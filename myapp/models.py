from django.db import models

# Create your models here.
class Post(models.Model):
	description=models.CharField(max_length=200)
	image=models.ImageField(upload_to='')