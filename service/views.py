from django.shortcuts import render

from service.models import Service , ServiceContent


def service(request):
    context = {
        "services": Service.objects.all(),
        "content": ServiceContent.objects.last()
    }
    return render(request, 'service.html', context)
