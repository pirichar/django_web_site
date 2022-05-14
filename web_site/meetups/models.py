from django.db import models
from django.forms import DateField

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


class Participant(models.Model):
	email = models.EmailField(unique=True)

	def __str__(self):
		return self.email


class Meetup(models.Model):
	title = models.CharField(max_length=200)
	organizer_email = models.EmailField()
	date = models.DateField()
	slug = models.SlugField(unique=True)
	description = models.TextField()
	image = models.ImageField(upload_to='images')
	#here we link the location model to our mettupmodel
	#foreignKey is for a one to many link
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	#to do a many to many relation between classes
	#we can use the models.ManyToManyField
	#this can be done in one of the class as we only do it here in meetup
	#by adding blank=True to the model we allow it to be empty
	#it couldve been added to any created model
	#it configure if a value MUST BE provided or not
	#null=True tell django that in the database table that it creates
	#this field can have a null entry which will append when an empty is blank
	participants = models.ManyToManyField(Participant, blank=True, null=True)
# this is a default method to add in python class
# to refer to the object created object as a string
	def __str__(self):
		return f'{self.title} - {self.slug}'

