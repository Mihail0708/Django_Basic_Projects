from django.shortcuts import render, redirect

from My_music_app.album.forms import AlbumForm, AlbumDeleteForm
from My_music_app.album.models import Album


def album_add(request):
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {'form': form}
    return render(request, 'add-album.html', context=context)


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)

    form = AlbumForm(instance=album)

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'album': album,
        'pk': pk,
    }
    return render(request, 'edit-album.html', context=context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        album.delete()
        return redirect('home page')

    form = AlbumDeleteForm(instance=album)
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'delete-album.html', context=context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'pk': pk,
        'album': album
    }
    return render(request, 'album-details.html', context=context)
