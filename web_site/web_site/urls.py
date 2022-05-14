"""web_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# in order to make django serv our image file we have to add stuff
# we have to concatnate the result of static to urlpatterns
# we use import static and impot settings to do so
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

#two different ways of doing things with Articles and meetup
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  RedirectView.as_view(url='/meetups')),
    path('meetups/', include('meetups.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
