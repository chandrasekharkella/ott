from django import forms
from.models import *
from multiselectfield import MultiSelectFormField

class movies_form(forms.ModelForm):
    class Meta:
        model=movies
        fields='__all__'
        labels = {
            'title': '',
            'cast': '',
            'year': '',

            'description': '',
            'actor_name': '',
            'director': '',

            'duration': '',
            'vedio_link': '',

        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie title'}),
            'cast': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie cast'}),
            'year': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie year'}),
            'actor_name': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the actor name'}),
            'director': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie director name'}),

            'description': forms.TextInput(
                attrs={'class': 'sign__input', 'placeholder': 'Enter the movie description'}),
            'banner': forms.FileInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie banner'}),
            'duration': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie duration'}),
            'vedio_link': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie link'}),
            'language': forms.Select(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie language'}),
            'category':forms.Select(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie catagory'}),
            'status':forms.Select(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie status'}),
            'geners': forms.Select(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie status'}),
        }




class publisher_form(forms.ModelForm):
    class Meta:
        model=movies
        fields = ('category','title','description','banner','language','geners','year','duration','director','actor_name','vedio_link')

        labels = {
            'title': '',
            'cast': '',
            'year': '',

            'description': '',
            'actor_name': '',
            'director': '',

            'duration': '',
            'vedio_link': '',

        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie title'}),
            'cast': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie cast'}),
            'year': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie year'}),
            'actor_name': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the actor name'}),
            'director': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie director name'}),

            'description': forms.TextInput(
                attrs={'class': 'sign__input', 'placeholder': 'Enter the movie description'}),
            'banner': forms.FileInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie banner'}),
            'duration': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie duration'}),
            'vedio_link': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie link'}),
            'language': forms.Select(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie language'}),
            'category':forms.Select(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie catagory'}),

            'geners': forms.Select(attrs={'class': 'sign__input', 'placeholder': 'Enter the movie status'}),
        }



# class add_catform(forms.ModelForm):
#     class Meta:
#         model=add_categories
#         fields='__all__'
#
#         category_choice = [('movie', 'movie'), ('show', 'show'), ('webseries', 'webseries'), ('kids', 'kids')]
#         language_choice = [('telugu', 'telugu'), ('hindi', 'hindi'), ('tamil', 'tamil'), ('malayalam', 'malayalam'),
#                            ('english', 'english')]
#         geners_choice = [('action', 'action'), ('adventure', 'adventure'), ('comedy', 'comedy'),
#                          ('horror', 'horror'), ('thirller', 'thirller'), ('sci fi', 'sci fi')]
#         status_choice = [('pending', 'pending'), ('approve', 'approve')]
#
#         widgets = {
#             'category': forms.Select(choices=category_choice, attrs={'class': 'sign__input'}),
#             'title': forms.TextInput(attrs={'class': 'sign__input'}),
#             'discription': forms.TextInput(attrs={'class': 'sign__input'}),
#             'image': forms.FileInput(attrs={'class': 'sign__input'}),
#             'language': forms.Select(choices=language_choice, attrs={'class': 'sign__input'}),
#             'geners': forms.Select(choices=geners_choice, attrs={'class': 'sign__input'}),
#             'screen_shot': forms.FileInput(attrs={'class': 'sign__input'}),
#             'movie_length': forms.TextInput(attrs={'class': 'sign__input'}),
#             'movie_director': forms.TextInput(attrs={'class': 'sign__input'}),
#             'actor_name': forms.TextInput(attrs={'class': 'sign__input'}),
#             'movie_link': forms.TextInput(attrs={'class': 'sign__input'}),
#             'status': forms.Select(choices=status_choice, attrs={'class': 'sign__input'}),
#
#
#         }

