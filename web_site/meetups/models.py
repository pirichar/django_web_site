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

# location couldve been added to meetup as a field but 
# adding it as a separate class (model) will ensure that
# it have its own database and that only 1 new york will be there

#then you have to relate location to meetup
# there is 3 different kind of relation u can have
# one to one = One author has one address, on adress belong to one author
# one to many = bone book as one author, one author wrote multiple books
#  many to many = a book can be published in many countries, a country can publish many books
# here its a one to many scenario because a meetup can have one location
# but a location can be used for many meetups 

class Location(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=300)

	def __str__(self):
		return f'{self.name} ({self.address})'

class Meetup(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	description = models.TextField()
	image = models.ImageField(upload_to='images')
	#here we link the location model to our mettupmodel
	#foreignKey is for a one to many link
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
# this is a default method to add in python class
# to refer to the object created object as a string
	def __str__(self):
		return f'{self.title} - {self.slug}'

