# Generated by Django 3.2.5 on 2021-07-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_alter_movies_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=20)),
                ('language', models.CharField(blank=True, choices=[('telugu', 'telugu'), ('hindi', 'hindi'), ('english', 'english')], max_length=20, null=True)),
            ],
        ),
    ]
