from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model


class MyCustomPasswordValidator:
    def validate(self, password: str, user: User | None):
        raise ValidationError("My custom validator")
