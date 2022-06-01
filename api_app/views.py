from django.shortcuts import render
from django.views.generic import TemplateView
from .services import get_droplets

class GetApi(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'droplets' : get_droplets(),
        }
        return context

# Create your views here.
