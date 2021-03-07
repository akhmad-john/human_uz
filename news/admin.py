from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass


class ContentBlockInline(admin.StackedInline):
    model = ContentBlock
    min_num = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):


    fields = ('sub_category', 'heading', 'main_image','subheading')
    inlines = [ContentBlockInline,]