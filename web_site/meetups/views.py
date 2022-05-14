from django.shortcuts import render

from .models import Meetup
from .forms import RegistrationForm
# Create your views here.
# I use the Meetup.objects which is a static field not a field defined by us but a field defined by the base class
#  this object field gives us rich query method
# all is a simple but powerfull query method which will fetch all the instences of this class stored in this database
# we could as well chain some methods like this Meetup.objects.all().order_by
def index(request):
	meetups = Meetup.objects.all()
	return render(request, 'meetups/index.html', {
		'meetups': meetups
	})


# here we use the try block to try and the except to catch so if someone enter an invalid slug
# we redirect him to a page instead of having an error
def meetup_details(request, meetup_slug):
	try:
		selected_meetup = Meetup.objects.get(slug=meetup_slug)
		if request.method == 'GET':	
			registration_form = RegistrationForm()
		else:
			registration_form = RegistrationForm(request.POST)
			if registration_form.is_valid():
				participant = registration_form.save()
				selected_meetup.participants.add(participant)
				

		return render(request, 'meetups/meetup-details.html', {
		'meetup_found': True,
		'meetup': selected_meetup,
		'form' : registration_form
		})
	except Exception as exc:
		return render(request, 'meetups/meetup-details.html', {
			'meetup_found': False
		})