from django.contrib import admin
from .models import Meetup

# Here we can tell django which models should be accessible through the admin pannel
# you first have to import it and then you can use it
# Register your models here.

admin.site.register(Meetup)