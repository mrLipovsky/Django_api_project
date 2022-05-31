from django.shortcuts import render
from django.views.generic import TemplateView

class GetApi(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        pass

# Create your views here.
