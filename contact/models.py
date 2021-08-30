from django.db import models


class ContactInfo(models.Model):
    address = models.TextField(max_length=200)
    email = models.EmailField()
    telefon = models.CharField(max_length=200)
    telefon_2 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.address


class Contact(models.Model):
    user = models.CharField(max_length=500)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.user
