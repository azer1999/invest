from django.contrib import admin

# Register your models here.
from about.models import AboutCard, AboutStep , AboutContent , AboutContentStep,AboutSecondCard , AboutCenterContent, AboutCenterStep

admin.site.register(AboutCard)
admin.site.register(AboutStep)
admin.site.register(AboutContent)
admin.site.register(AboutContentStep)
admin.site.register(AboutSecondCard)
admin.site.register(AboutCenterContent)
admin.site.register(AboutCenterStep)