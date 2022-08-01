from django.db import models

# Create your models here.


from ckeditor.fields import RichTextField
# import the user table
from django.contrib.auth.models import User


class Blog(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	content = RichTextField()

	def __str__(self):
		return self.title


