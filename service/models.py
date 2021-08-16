from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField()
    text = models.TextField()

    def __str__(self):
        return self.title