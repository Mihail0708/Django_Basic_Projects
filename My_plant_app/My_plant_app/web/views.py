from django.shortcuts import render, redirect

from My_plant_app.web.forms import ProfileForm, PlantForm, PlantDeleteForm, ProfileEditForm
from My_plant_app.web.models import Profile, Plant


def get_profile():
    try:
        profile = Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None

    return profile


def home_page(request):
    profile = get_profile()

    context = {'profile': profile}

    return render(request, 'home-page.html', context=context)


def catalogue(request):
    profile = get_profile()
    plants = Plant.objects.all()
    context = {'plants': plants, 'profile': profile}
    return render(request, 'catalogue.html', context=context)


def profile_create(request):
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context=context)


def profile_edit(request):
    profile = get_profile()

    form = ProfileEditForm(instance=profile)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'profile/edit-profile.html', context=context)


def profile_delete(request):
    profile = get_profile()
    plants = Plant.objects.all()
    if request.method == 'POST':
        profile.delete()
        plants.delete()
        return redirect('home page')

    context = {'profile': profile}
    return render(request, 'profile/delete-profile.html', context=context)


def profile_details(request):
    profile = get_profile()
    plants = Plant.objects.all()
    context = {
        'profile': profile,
        'plants': plants
    }
    return render(request, 'profile/profile-details.html', context=context)


def plant_details(request, pk):
    profile = get_profile()
    plant = Plant.objects.filter(pk=pk).get()

    context = {
        "profile": profile,
        'plant': plant
    }
    return render(request, 'plant/plant-details.html', context=context)


def plant_create(request):
    profile = get_profile()
    form = PlantForm()

    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'plant/create-plant.html', context=context)


def plant_edit(request, pk):
    profile = get_profile()
    plant = Plant.objects.filter(pk=pk).get()
    form = PlantForm(instance=plant)

    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form,
        'plant': plant
    }
    return render(request, 'plant/edit-plant.html', context=context)


def plant_delete(request, pk):
    profile = get_profile()
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')

    form = PlantDeleteForm(instance=plant)
    context = {
        'profile': profile,
        'form': form,
        'pk': pk
    }
    return render(request, 'plant/delete-plant.html', context=context)
