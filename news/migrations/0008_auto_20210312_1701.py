# Generated by Django 3.1.6 on 2021-03-12 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_article_uz_heading'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='uz_heading',
            new_name='oz_heading',
        ),
    ]
