# Generated by Django 3.2.5 on 2021-07-27 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_auto_20210727_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('approve', 'approve')], default='pending', max_length=500),
        ),
    ]
