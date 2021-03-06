from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    email and last_name and first_name and password are required.
    Other fields are optional.
    """
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
