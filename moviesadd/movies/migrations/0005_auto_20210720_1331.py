# Generated by Django 3.2.5 on 2021-07-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20210717_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='banner',
            field=models.ImageField(null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
