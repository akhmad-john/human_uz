from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'subcategories'


class Article(models.Model):
    heading = models.CharField(max_length=50)
    subheading = models.TextField()
    text = HTMLField()

    