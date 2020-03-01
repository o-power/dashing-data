#from django.conf.urls import url
#from django.core.urlresolvers import reverse_lazy
#from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
# password_reset: Form where the user submits the email address
# password_reset_done: Page displayed to the user after submitting the email form. 
#     Usually with instructions to open the email account, look in the spam folder etc. 
#     And asking for the user to click on the link he will receive.
# password_reset_confirm: The link that was emailed to the user. 
#     This view will validate the token and display a password form if the token is valid 
#     or an error message if the token is invalid (e.g. was already used or expired).
# password_reset_complete: Page displayed to the user after the password was successfully changed.

urlpatterns = [
    # django.contrib.auth.views.password_reset will be called for URLs
    # matching '/accounts/password/reset' with the keyword 
    # argument post_reset_redirect = reverse_lazy('password_reset_done').
    # url(r'^$',
    #     password_reset,
    #     {'post_reset_redirect': reverse_lazy('password_reset_done')},
    #     name = 'password_reset'),
    # url(r'^done/$',
    #     password_reset_done,
    #     name = 'password_reset_done'),
    # url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    #     password_reset_confirm,
    #     {'post_reset_redirect': reverse_lazy('password_reset_complete')},
    #     name = 'password_reset_confirm'),
    # url(r'^complete/$',
    #     password_reset_complete,
    #     name = 'password_reset_complete')    
]

# From the documentation:
#def url(regex, view, kwargs=None, name=None):
#    return re_path(regex, view, kwargs, name)