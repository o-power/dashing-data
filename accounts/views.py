from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages, auth
from django.urls import reverse

def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            # This save creates a user in the database
            registration_form.save()

            #user = auth.authenticate(request.POST.get('email'),
            #                        password=request.POST.get('password1'))
            user = auth.authenticate(username=request.POST.get('username'),
                                    password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        registration_form = UserRegistrationForm()

    context = {'registration_form': registration_form}
    return render(request, 'register.html', context)