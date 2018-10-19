### Requirements
This example assumes that you have `Django` and `pwnedapi` installed and the Django project contains app named `django_pwnedapi`.
### Validator
File: `django_pwnedapi/validators.py`  
***
A Django validator is a callable that takes a value and raises `ValidationError` if it doesn’t meet some criteria, in this example - if password has been reported as seen by `pwnedapi`.  
Code:
```python
def pwnedapi_validator(value):
    password = Password(value)
    if password.is_pwned():
        count = password.pwned_count
        raise ValidationError(
            'Password has been seen %(count)d times before!',
            'leaked',
            params={'count': count}
        )
```
[Example](django_pwnedapi/validators.py), class-based with default params, serialization decorator and Django `gettext` string wrap
### Form
File: `django_pwnedapi/forms.py`
***
A Django form fields can add custom validators, such as created earlier `pwnedapi_validator`
Code:
```python
class SimplePwnedAPIForm(forms.Form):
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput, 
        validators=[pwnedapi_validator]
    )
```
[Example with class-based validator](django_pwnedapi/forms.py)
### View
File: `django_pwnedapi/views.py`
***
View has to check or create the form and return correct response.  
Code:
```python
def pwnedapi_view(request):
    if request.method == 'POST':
        form = SimplePwnedAPIForm(request.POST)
        if form.is_valid():
            return render(request, 'django_pwnedapi/pwnedapi_form.html', context={'form': form, 'valid': True})
    else:
        form = SimplePwnedAPIForm()
    return render(request, 'django_pwnedapi/pwnedapi_form.html', context={'form': form})
```
[Example](django_pwnedapi/views.py)
### URLs
File: `django_pwnedapi/urls.py`
***
`/pwnedapi` URL path for Django. The usual.  
Code:
```python
urlpatterns = [
    path('pwnedapi/', pwnedapi_view, name='pwnedapi')
]
```
[Example](django_pwnedapi/urls.py)
### Template
File: `django_pwnedapi/templates/django_pwnedapi/pwnedapi_form.html`
***
Basic template with form and success message:
```html
<html>
<head>
    <meta charset="utf-8">
    <title>PwnedAPI Form</title>
</head>
    <body>
        {% if valid %}
            <h3>No pwnage found!</h3>
        {% endif %}
        <form method="post">
            {% csrf_token %}
            {{ form }}
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```
[Example](django_pwnedapi/templates/django_pwnedapi/pwnedapi_form.html)
