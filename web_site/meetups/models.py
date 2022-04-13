from django.db import models

# Create your models here.

# all the custom models need to unherit of the models.model class
# think at the model instances as object you will be working with in your code


# class is the function from django
# models is the library I imported line 1
# Model is the function from that library to create custom models
# title is an attribute
# slug is an attribute
# description is an attribute

# Django will take your define models and will automatically create 
# data base tables in that sqlite database out of the box
# and will createa one table per model in that data base

class Meetup(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	description = models.TextField()
