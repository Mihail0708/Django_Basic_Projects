from django import forms

from My_plant_app.web.models import Profile, Plant


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name'}


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'profile_picture': 'Profile Picture'}


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'plant_type': 'Type',
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'price': 'Price',
        }


class PlantDeleteForm(PlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
