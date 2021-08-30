from django.db import models



class FAQ(models.Model):
    question = models.CharField(max_length=150)
    answer = models.TextField(max_length=500)
    def  __str__(self):
        return self.question

class Category(models.Model):
    title = models.CharField(max_length=150)
    faq = models.ManyToManyField(FAQ)

    def __str__(self):
        return self.title
