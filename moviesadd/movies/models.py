from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.


class movies(models.Model):
    lang_choices = [('telugu', 'telugu'), ('hindi', 'hindi'), ('english', 'english')]
    category_choice = [('movie', 'movie'), ('show', 'show'), ('webseries', 'webseries'), ('Cartoon', 'cartoon')]
    geners_choice = [('action', 'action'), ('adventure', 'adventure'), ('comedy', 'comedy'),
                     ('horror', 'horror'), ('thirller', 'thirller'), ('sci fi', 'sci fi')]
    # status_choice = [('pending', 'pending'), ('approve', 'approve')]

    title=models.CharField(max_length=200)
    banner =models.ImageField(upload_to='static/images',null=True)
    actor_name = models.CharField(max_length=1000, null=True, blank=True)
    director = models.CharField(max_length=200, null=True, blank=True)
    vedio_link = models.CharField(max_length=500)
    year = models.IntegerField()

    description = models.CharField(max_length=1000)
    duration = models.CharField(max_length=20)
    category = models.CharField(max_length=500, choices=category_choice,blank=True,null=True)
    geners = models.CharField(max_length=500, choices=geners_choice, blank=True, null=True)
    language=  models.CharField(max_length=20, choices=lang_choices,blank=True,null=True)
    status = models.BooleanField(default=0)
    def __str__(self):
        return self.title







# Publishers Models


# class add_categories(models.Model):
#     category_choice = [('movie', 'movie'), ('show', 'show'), ('webseries', 'webseries'), ('kids', 'kids')]
#     language_choice = [('telugu', 'telugu'), ('hindi', 'hindi'), ('tamil', 'tamil'), ('malayalam', 'malayalam'),
#                        ('english', 'english')]
#     geners_choice = [('action', 'action'), ('adventure', 'adventure'), ('comedy', 'comedy'),
#                      ('horror', 'horror'), ('thirller', 'thirller'), ('sci fi', 'sci fi')]
#     status_choice = [('pending', 'pending'), ('approve', 'approve')]
#     category=models.CharField(max_length=500,choices=category_choice)
#     title=models.CharField(max_length=500)
#     discription = models.TextField(max_length=10000, null=True, blank=True)
#     image = models.ImageField(upload_to='static/images', null=True, blank=True)
#     language=models.CharField(max_length=500,choices=language_choice)
#     geners=models.CharField(max_length=500,choices=geners_choice)
#     screen_shot = models.ImageField(upload_to='static/images', null=True, blank=True)
#     movie_length = models.CharField(max_length=50, null=True, blank=True)
#     movie_director = models.CharField(max_length=200, null=True, blank=True)
#     actor_name = models.CharField(max_length=1000, null=True, blank=True)
#     movie_link = models.TextField(max_length=10000, null=True, blank=True)
#     status=models.CharField(max_length=500,choices=status_choice)
#
#     def __str__(self):
#         return self.title

class main_banner(models.Model):
    title = models.CharField(max_length=200)

    banner_image= models.ImageField(upload_to='static/images', null=True)
    def __str__(self):
        return self.title


