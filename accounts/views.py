from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages, auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def register(request):
    """A view that manages the registration form."""
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            # create the user in the database
            registration_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                    password=request.POST.get('password1'))

            if user is not None:
                # save user id in the session
                auth.login(request, user)
                messages.success(request, 'You have successfully registered.')

                if request.GET and request.GET.get('next') != '':
                    next = request.GET.get('next')
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                messages.error(request, 'Unable to log you in at this time!')
    else:
        registration_form = UserRegistrationForm()

    context = {'registration_form': registration_form, 'next': request.GET.get('next', '')}
    return render(request, 'register.html', context)

@login_required
def profile(request):
    """A view that displays the profile page of a logged in user."""
    return render(request, 'profile.html')

@login_required
def logout(request):
    """A view that logs the user out and redirects back to the index page."""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect(reverse('index'))

def login(request):
    """A view that manages the login form."""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(request.POST.get('username_or_email'),
                                    password=request.POST.get('password'))

            if user is not None:
                # save user id in the session
                auth.login(request, user)
                messages.error(request, 'You have successfully logged in.')

                if request.GET and request.GET.get('next') != '':
                    next = request.GET.get('next')
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                login_form.add_error(None, 'Your username or password are incorrect.')
    else:
        login_form = UserLoginForm()

    context = {'login_form': login_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', context)