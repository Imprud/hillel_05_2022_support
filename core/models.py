from typing import Optional

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models


class TimeStampMixin:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUserManager(UserManager):
    """Custom user manager."""

    def create_user(self, email, username=None, password=None, **kwargs):
        if not email:
            raise ValueError("Email field is required.")
        if not password:
            raise ValueError("Password field is required.")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email: str,
        user: Optional[str] = None,
        password: Optional[str] = None,
        **kwargs
    ):
        super_user_payload = {"is_superuser": True, "is_active": True, "is_staff": True}
        return self.create_user(email, user, password, **super_user_payload)


class User(AbstractBaseUser, PermissionsMixin, TimeStampMixin):
    """This is my custom user model."""

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    phone = models.CharField(max_length=13, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = EMAIL_FIELD
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
