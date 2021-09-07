from django.contrib import admin

# Register your models here.
from account.models import Investor, UserPanel

admin.site.register(Investor)
admin.site.register(UserPanel)
