# Generated by Django 2.2.28 on 2023-03-04 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmr', '0002_recipe_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
