"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# add to the top
from django.contrib.auth.views import (
   password_reset, 
   password_reset_done,
   password_reset_confirm,
   password_reset_complete
)
from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import TemplateView
from collection import views #hellowebapp

urlpatterns = [
	url(r'^$', views.index, name='home'), #hellowebapp

	# The new URL entries we're adding:
	url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^contact/$', 
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
 	url(r'^things/(?P<slug>[-\w]+)/$', views.thing_detail, 
        name='thing_detail'),
 	 # new line we're adding!
    url(r'^things/(?P<slug>[-\w]+)/edit/$', 
        views.edit_thing,
        name='edit_thing'),

     # the new password reset URLs
    url(r'^accounts/password/reset/$', 
        password_reset,
        {'template_name':
        'registration/password_reset_form.html'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name':
        'registration/password_reset_done.html'},
        name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        password_reset_confirm,
        {'template_name':
        'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$', 
        password_reset_complete,
        {'template_name':
        'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    url(r'^accounts/',
        include('registration.backends.simple.urls')),
  
    url(r'^admin/', admin.site.urls),
]
