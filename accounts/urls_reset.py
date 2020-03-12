#from django.core.urlresolvers import reverse_lazy
#from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

# from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
# from django.contrib.auth.views import password_change, password_change_done

#accounts/password_change/ [name='password_change']
#accounts/password_change/done/ [name='password_change_done']
#accounts/password_reset/ [name='password_reset']
#accounts/password_reset/done/ [name='password_reset_done']
#accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
#accounts/reset/done/ [name='password_reset_complete']

urlpatterns = [
    # form where the user submits the email address to generate the reset email
    path(
        '',
        auth_views.PasswordResetView.as_view(success_url='done/'),
        name='password_reset'
    ),
    # password_reset_done: Page displayed to the user after submitting the email form. 
    # Usually with instructions to open the email account, look in the spam folder etc. 
    # And asking for the user to click on the link he will receive.
    path(
        'done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    # password_reset_confirm: The link that was emailed to the user. 
    # This view will validate the token and display a password form if the token is valid 
    # or an error message if the token is invalid (e.g. was already used or expired).
    path(
        '<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')),
        name='password_reset_confirm'
    ),
    # password_reset_complete: Page displayed to the user after the password was successfully changed.
    path(
        'complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]