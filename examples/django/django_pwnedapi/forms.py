from django import forms
from django.utils.translation import gettext_lazy as _
from .validators import PwnedAPIValidator


class SimplePwnedAPIForm(forms.Form):
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput, validators=[PwnedAPIValidator()])
