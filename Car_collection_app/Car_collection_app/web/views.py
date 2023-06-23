from django.shortcuts import render, redirect

from Car_collection_app.web.forms import ProfileForm, CarForm, CarDeleteForm, ProfileEditForm
from Car_collection_app.web.models import Profile, Car


def get_profile():
    try:
        profile = Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None

    return profile


def home_page(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'index.html', context=context)


def catalogue(request):
    profile = get_profile()
    cars = Car.objects.all()
    context = {
        'cars': cars,
        'profile': profile
    }
    return render(request, 'catalogue.html', context=context)


def profile_create(request):
    form = ProfileForm()
    profile = get_profile()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'profile/profile-create.html', context=context)


def profile_delete(request):
    profile = get_profile()
    cars = Car.objects.all()

    if request.method == 'POST':
        profile.delete()
        cars.delete()
        return redirect('home page')

    context = {
        'profile': profile
    }
    return render(request, 'profile/profile-delete.html', context=context)


def profile_details(request):
    profile = get_profile()
    cars = Car.objects.all()
    sum = 0
    name = ''

    if profile.first_name:
        name += profile.first_name
    if profile.last_name:
        name += ' ' + profile.last_name
    for car in cars:
        sum += car.price
    context = {'profile': profile, 'sum': sum, 'name': name}
    return render(request, 'profile/profile-details.html', context=context)


def profile_edit(request):
    profile = get_profile()
    form = ProfileEditForm(instance=profile)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/profile-edit.html', context=context)


def car_create(request):
    profile = get_profile()
    form = CarForm()

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'car/car-create.html', context=context)


def car_delete(request, pk):
    profile = get_profile()
    car = Car.objects.filter(id=pk).get()
    form = CarDeleteForm(instance=car)

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
        'profile': profile
    }
    return render(request, 'car/car-delete.html', context=context)


def car_details(request, pk):
    profile = get_profile()
    car = Car.objects.filter(id=pk).get()
    context = {'car': car, 'profile': profile}
    return render(request, 'car/car-details.html', context=context)


def car_edit(request, pk):
    profile = get_profile()
    car = Car.objects.filter(id=pk).get()
    form = CarForm(instance=car)

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile,
        'car': car,
    }
    return render(request, 'car/car-edit.html', context=context)