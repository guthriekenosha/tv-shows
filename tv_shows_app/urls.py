from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('add_show', add_show),
    path('create_show', create_show),
    path('shows', all_shows),
    path('shows/<int:id>/edit_show', edit_show),
    path('shows/<int:id>/update', update),
    path('shows/<int:id>/new_show', new_show),
    path('shows/<int:id>/delete', delete),
]