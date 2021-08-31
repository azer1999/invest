from about.models import AboutStep, AboutCard, AboutContent, AboutContentStep, AboutSecondCard, AboutCenterContent, \
    AboutCenterStep
from core.models import SocialMedia


def main(request):
    context = {
        "about_steps": AboutStep.objects.all(),
        "about_card": AboutCard.objects.all(),
        "content": AboutContent.objects.last(),
        "content_step": AboutContentStep.objects.all(),
        "second_card": AboutSecondCard.objects.all(),
        "center_content": AboutCenterContent.objects.last(),
        "center_step_left": AboutCenterStep.objects.all()[:3],
        "center_step_right": AboutCenterStep.objects.all()[3:],
        "media": SocialMedia.objects.all(),
    }
    return context
