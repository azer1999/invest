from django.shortcuts import render

from .models import FAQ , Category


def faq(request):
     context = {
         "faq": FAQ.objects.all(),
         "categories": Category.objects.all()
     }
     return render(request, "faq.html" , context)
