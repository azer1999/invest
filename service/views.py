from django.shortcuts import render

from service.models import Service


def service(request):
    context = {
        "services": Service.objects.all(),
    }
    return render(request, 'service.html', context)
