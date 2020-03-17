from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend
from django.db.models import Q

class CaseInsensitiveAuth(BaseBackend):
    """
    Authenticates user using a case insensitive match on username or email.
    """
    def authenticate(self, username_or_email=None, password=None):
        """
        Return an instance of User using the supplied username
        or email (case insensitive) and verify the password.
        """
        users = User.objects.filter(Q(username__iexact=username_or_email) |
                                    Q(email__iexact=username_or_email))
        
        if not users:
            return None

        user = users[0]
        
        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        """
        Used by the Django authentication system to retrieve a User instance.
        """
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None