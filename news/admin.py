from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin
from django_tabbed_changeform_admin.admin import DjangoTabbedChangeformAdmin
from fieldsets_with_inlines import FieldsetsInlineMixin
# from betterforms.forms import BetterForm, Fieldset

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
class ArticleAdmin(FieldsetsInlineMixin, admin.ModelAdmin):
    # fields = ( 'ru_heading', )



    fieldsets  = (
        ('Русский', {
            'classes': ('wide', 'collapse'),
            'fields': ('sub_category', 'ru_heading', 'main_image','ru_subheading',),
            # 'inlines': ('ContentBlockInline',)
        },
        ),
        
    )

    # fields = ('sub_category', 'ru_heading', 'main_image','subheading')
    # inlines = [ContentBlockInline,]