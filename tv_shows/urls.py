
from django.urls import path, include
from tv_shows_app import views
urlpatterns = [
    # path('', views.add_show),
    path('', include('tv_shows_app.urls')),
]

