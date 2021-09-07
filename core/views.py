from django.shortcuts import render

from core.models import MainInfo, Counter, WhoWeAre, Partner


def index(request):
    context = {}
    context['main_info'] = MainInfo.objects.last()
    context['counter'] = Counter.objects.all()
    context['who'] = WhoWeAre.objects.last()
    context['partners'] = Partner.objects.all()
    return render(request, 'index.html', context)



