from django.urls import path

from .views import HomePage, ImageListView


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('images/', ImageListView.as_view(), name='images')
]
