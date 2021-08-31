from django.shortcuts import render

from .models import AboutCard, AboutStep, AboutContent, AboutContentStep, AboutSecondCard, AboutCenterContent, \
    AboutCenterStep


def about(request):
    return render(request, 'about.html')


def index(request):
    contex = {
        "about_steps": AboutStep.objects.all(),
        "about_card": AboutCard.objects.all(),
        "content": AboutContent.objects.last(),
        "content_step": AboutContentStep.objects.all(),
        "second_card": AboutSecondCard.objects.all(),
        "center_content": AboutCenterContent.objects.last(),
        "center_step_left": AboutCenterStep.objects.all()[:3],
        "center_step_right": AboutCenterStep.objects.all()[3:],
    }
    return render(request, 'index.html', contex)
