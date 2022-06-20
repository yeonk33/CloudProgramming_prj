from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return f'/category/{self.slug}/'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/tag/{self.slug}/'


class Todo(models.Model):
    todo = models.CharField(max_length=30)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    deadline = models.DateTimeField(null=True)

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.todo

    def get_absolute_url(self):
        return f'/{self.pk}/'
