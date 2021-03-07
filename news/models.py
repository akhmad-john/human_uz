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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'subcategories'


class Article(models.Model):
    main_image = models.ImageField(upload_to='main_images')
    heading = models.CharField(max_length=50)
    subheading = models.TextField()
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.heading

class ContentBlock(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='content_blocks')
    content =  HTMLField()
    block_image = models.ImageField(upload_to='images')
