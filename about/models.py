from django.db import models


# Create your models here.
class AboutCard(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField(upload_to='about/images/')
    text = models.TextField()

    def __str__(self):
        return self.title


class AboutStep(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField(upload_to='about/images/')
    text = models.TextField()

    def __str__(self):
        return self.title


class AboutContent(models.Model):
    title = models.CharField(max_length=55)
    text = models.TextField()
    button_text = models.CharField(max_length=55)
    button_url = models.URLField()

    def __str__(self):
        return self.title


class AboutContentStep(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class AboutSecondCard(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField(upload_to='about/images/')
    text = models.TextField()

    def __str__(self):
        return self.title


class AboutCenterContent(models.Model):
    title = models.CharField(max_length=55)
    text = models.TextField()

    def __str__(self):
        return self.title


class AboutCenterStep(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField(upload_to='about/images/')
    text = models.TextField()

    def __str__(self):
        return self.title

