from django.contrib import admin
from .models import Meetup, Location

# Here we can tell django which models should be accessible through the admin pannel
# you first have to import it and then you can use it
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug')
	list_filter = ('title', 'slug', 'location')
	prepopulated_fields = {'slug': ('title', )}

admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)