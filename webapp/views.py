# coding: utf-8

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.contrib.auth.decorators import login_required


import account.views
import account.forms

from models import *
from django.contrib import messages


def home(request):
    text = 'Ahoj'

    # email = EmailMessage('Hello', 'Body goes here', 'robert,lacina@seznam.cz',
    #         ['robert.lacina@gmail.com', ], ['robert.lacina@gmail.com'],
    #          headers={'Message-ID': 'foo'})
    # email.send()
    form = account.forms.LoginUsernameForm

    return render_to_response('home.html', {'text': text, 'login_form': form, },
                              context_instance=RequestContext(request))

def profile_saved(request):

    form = account.forms.LoginUsernameForm

    return render_to_response('home.html', {'login_form': form, },
                              context_instance=RequestContext(request))


@login_required
def profile(request):
    form = UserProfileForm()

    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        profile = UserProfile.objects.get(user=request.user.id)
        profile_form = UserProfileForm(data=request.POST,instance=profile)

        #print profile_form
        # If the two forms are valid...
        if profile_form.is_valid():
            profile = UserProfile.objects.get(user=request.user.id)
            profiles = profile_form.save(commit=False)
            print profiles

            profiles.save()
            return render_to_response('profile_saved.html', {'profile_form': profile_form, },
                              context_instance=RequestContext(request))
            # Update our variable to tell the template registration was successful.

        else:
            print 'dddd'
            print profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        profile = UserProfile.objects.get(user=request.user.id)
        profile_form = UserProfileForm(instance=profile)
        print profile

    return render_to_response('profile.html', {'profile_form': profile_form, },
                              context_instance=RequestContext(request))