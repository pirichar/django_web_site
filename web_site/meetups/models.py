from django.db import models

# Create your models here.

# all the custom models need to unherit of the models.model class
# think at the model instances as object you will be working with in your code

# Django will take your define models and will automatically create 
# data base tables in that sqlite database out of the box
# and will createa one table per model

class Meetup(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	description = models.TextField()
