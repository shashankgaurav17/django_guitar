from django import forms

from .models import Details

class PostForm(forms.ModelForm):

    class Meta:
        model = Details
        fields = ('song_name', 'cappo', 'language','type','url','lyrics')