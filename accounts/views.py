from django.shortcuts import redirect, render
from .models import Profile
from .forms import UserForm, ProfileForm, UserCreateForm, AddListingForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from property.models import PropertyBook, Property
from django.views.generic.edit import CreateView

# Create your views here.


def signup(request):
    if request.method == 'POST':
        signup_form = UserCreateForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            # return redirect(reverse('login'))
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('accounts:profile'))

    else:
        signup_form = UserCreateForm()

    return render(request, 'registration/signup.html', {'signup_form': signup_form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile/profile.html', {'profile': profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_form = profile_form.save(commit=False)
            my_form.user = request.user
            my_form.save()
            messages.success(request, 'Profile details updated.')
            return redirect(reverse('accounts:profile'))

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'profile/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def myreservations(request):
    property_list = PropertyBook.objects.filter(user=request.user)
    return render(request, 'profile/reservations.html', {'property_list': property_list})


def mylisting(request):
    property_list = Property.objects.filter(owner=request.user)
    return render(request, 'profile/mylisting.html', {'property_list': property_list})


def add_listing(request):
    if request.method == 'POST':
        add_listing_form = AddListingForm(
            request.POST, request.FILES)

        if add_listing_form.is_valid():
            my_form = add_listing_form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            messages.success(request, 'A new listing was created.')
            return redirect(reverse('accounts:listing'))

    else:
        add_listing_form = AddListingForm()

    return render(request, 'profile/add_listing.html', {
        'add_listing_form': add_listing_form
    })
