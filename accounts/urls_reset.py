from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

urlpatterns = [
    # password_reset: form where the user submits the email address to generate the reset email.
    path(
        '',
        auth_views.PasswordResetView.as_view(success_url='done/'),
        name='password_reset'
    ),
    # password_reset_done: page displayed to the user after submitting the email form.
    path(
        'done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    # password_reset_confirm: the link that was emailed to the user. 
    # This view will validate the token and display a password form if the token is valid 
    # or an error message if the token is invalid (e.g. was already used or expired).
    path(
        '<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')),
        name='password_reset_confirm'
    ),
    # password_reset_complete: page displayed to the user after the password was successfully changed.
    path(
        'complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]