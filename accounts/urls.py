from django.urls import path
from .views import profile, profile_edit, signup, myreservations, mylisting, add_listing


app_name = 'accounts'

urlpatterns = [
    path('signup', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('reservations/', myreservations, name='reservations'),
    path('listing/', mylisting, name='listing'),
    path('profile/edit', profile_edit, name='profile_edit'),
    path('profile/addlisting', add_listing, name='add_listing'),
]
