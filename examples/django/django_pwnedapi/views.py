from django.shortcuts import render
from .forms import SimplePwnedAPIForm


def pwnedapi_view(request):
    if request.method == 'POST':
        form = SimplePwnedAPIForm(request.POST)
        if form.is_valid():
            return render(
                request,
                'django_pwnedapi/pwnedapi_form.html',
                context={'form': form, 'valid': True}
            )
    else:
        form = SimplePwnedAPIForm()
    return render(request, 'django_pwnedapi/pwnedapi_form.html', context={'form': form})
