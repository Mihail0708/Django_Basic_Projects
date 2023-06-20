from django.shortcuts import render, redirect

from My_music_app.album.models import Album
from My_music_app.user_profile.forms import ProfileForm
from My_music_app.user_profile.models import Profile


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def home_page(request):
    profile = get_profile()

    if profile is None:
        form = ProfileForm()
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home page')

        context = {
            'form': form,
            'hide_nav': True,
        }
        return render(request, 'home-no-profile.html', context=context)

    context = {
        'albums': Album.objects.all(),
    }
    return render(request, 'home-with-profile.html', context=context)


