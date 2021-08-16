from django.shortcuts import render
from .forms import ContactForm
from .models import ContactInfo


def contact(request):
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Данные были введены неправильно!'
    form = ContactForm()
    context = {
        "info": ContactInfo.objects.last(),
        'form': form,
        'error': error

    }

    return render(request, 'contact.html', context)
