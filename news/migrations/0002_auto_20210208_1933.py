# Generated by Django 3.1.6 on 2021-02-08 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'subcategories'},
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='news.category'),
            preserve_default=False,
        ),
    ]
