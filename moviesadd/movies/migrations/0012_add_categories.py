# Generated by Django 3.2.5 on 2021-07-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_delete_add_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('movie', 'movie'), ('show', 'show'), ('webseries', 'webseries'), ('kids', 'kids')], max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('discription', models.TextField(blank=True, max_length=10000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('language', models.CharField(choices=[('telugu', 'telugu'), ('hindi', 'hindi'), ('tamil', 'tamil'), ('malayalam', 'malayalam'), ('english', 'english')], max_length=500)),
                ('geners', models.CharField(choices=[('action', 'action'), ('adventure', 'adventure'), ('comedy', 'comedy'), ('horror', 'horror'), ('thirller', 'thirller'), ('sci fi', 'sci fi')], max_length=500)),
                ('screen_shot', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('movie_length', models.CharField(blank=True, max_length=50, null=True)),
                ('movie_director', models.CharField(blank=True, max_length=200, null=True)),
                ('actor_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('movie_link', models.TextField(blank=True, max_length=10000, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('approve', 'approve')], max_length=500)),
            ],
        ),
    ]
