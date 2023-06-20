from django.shortcuts import render, redirect

from My_music_app.album.models import Album
from My_music_app.user_profile.models import Profile


def profile_details(request):
    profile = Profile.objects.get()
    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums': albums
    }
    return render(request, 'profile-details.html', context=context)


def profile_delete(request):
    profile = Profile.objects.get()
    albums = Album.objects.all()
    if request.method == 'POST':
        profile.delete()
        albums.delete()
        return redirect('home page')
    return render(request, 'profile-delete.html')


