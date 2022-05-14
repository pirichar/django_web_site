from django.shortcuts import render
from django.shortcuts import redirect

from .models import Participant
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
				user_mail = registration_form.cleaned_data['email']
				participant, _ = Participant.objects.get_or_create(email=user_mail)
				selected_meetup.participants.add(participant)
				return redirect('confirm-registration', meetup_slug=meetup_slug)
				
		return render(request, 'meetups/meetup-details.html', {
		'meetup_found': True,
		'meetup': selected_meetup,
		'form' : registration_form
		})
	except Exception as exc:
		print(exc)
		return render(request, 'meetups/meetup-details.html', {
			'meetup_found': False
		})

def confirm_registration(request, meetup_slug):
		meetup = Meetup.objects.get(slug=meetup_slug)
		return render(request, 'meetups/registration-success.html',
		{'organizer_email': meetup.organizer_email})