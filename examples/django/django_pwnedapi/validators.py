from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

from pwnedapi import Password


@deconstructible
class PwnedAPIValidator:
    code = 'leaked'
    message = _('Password has been seen %(count)d times before!')

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        password = Password(value)
        if password.is_pwned():
            count = password.pwned_count
            raise ValidationError(
                self.message,
                self.code,
                params={'count': count}
            )
