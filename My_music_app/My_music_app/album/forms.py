from django import forms

from My_music_app.album.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={'placeholder': 'Album Name'}
            ),
            'artist': forms.TextInput(
                attrs={'placeholder': 'Artist'}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Description'}
            ),
            'image_URL': forms.URLInput(
                attrs={'placeholder': 'Image URL'}
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': 'Price'}
            )
        }
        labels = {
            'album_name': 'Album Name',
        }


class AlbumDeleteForm(AlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'