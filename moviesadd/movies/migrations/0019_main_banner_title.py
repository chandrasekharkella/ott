# Generated by Django 3.2.5 on 2021-07-27 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_main_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_banner',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
