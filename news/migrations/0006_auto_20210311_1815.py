# Generated by Django 3.1.6 on 2021-03-11 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_main_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='heading',
            new_name='ru_heading',
        ),
    ]
