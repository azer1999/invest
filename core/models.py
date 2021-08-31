from django.db import models


# Create your models here.

class Partner(models.Model):
    image = models.ImageField(upload_to='partner/images/')

    def __str__(self):
        return f'{self.id}'


class WhoWeAre(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='who/images/')

    def __str__(self):
        return f'{self.id}'


class MainInfo(models.Model):
    image = models.ImageField(upload_to='main/images/')
    top = models.CharField(max_length=55)
    title = models.CharField(max_length=55)
    subtitle = models.CharField(max_length=55)
    btn_text = models.CharField(max_length=55)
    btn_url = models.URLField()

    def __str__(self):
        return f'{self.title}'


class Counter(models.Model):
    icon = models.ImageField(upload_to='icons/')
    number = models.CharField(max_length=55)
    subtitle = models.CharField(max_length=55)

    def __str__(self):
        return f'{self.subtitle}'


class SocialMedia(models.Model):
    media_types = (
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('youtube', 'YouTube')
    )
    media = models.CharField(choices=media_types, max_length=55, unique=True)
    url = models.URLField()

    def __str__(self):
        return f'{self.media}'
