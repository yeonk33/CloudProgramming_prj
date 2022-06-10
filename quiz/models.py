from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=100)

    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)

    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question