from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import ImageModel


class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        context['active'] = 'home'
        return context


class ImageListView(ListView):
    model = ImageModel
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super(ImageListView, self).get_context_data(**kwargs)
        context['active'] = 'images'
        return context
