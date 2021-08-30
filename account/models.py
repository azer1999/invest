from django.contrib.auth.models import User
from django.db import models


class Investor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    front_passport = models.ImageField(upload_to='investor/passports')
    back_passport = models.ImageField(upload_to='investor/passports')
    selfie_passport = models.ImageField(upload_to='investor/passports')


    phone = models.CharField(max_length=55)


    def __str__(self):
        return f'{self.user.first_name} -  {self.user.last_name}'