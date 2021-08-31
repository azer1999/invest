from django.contrib import admin

# Register your models here.
from core.models import Counter, MainInfo, Partner, WhoWeAre, SocialMedia

admin.site.register(Counter)
admin.site.register(MainInfo)
admin.site.register(Partner)
admin.site.register(WhoWeAre)
admin.site.register(SocialMedia)
