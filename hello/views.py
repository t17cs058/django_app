from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Hello

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwagrs):
        context = super().get_context_data(**kwagrs)
        context['one_name'] = Hello.objects.all()[0]
        return context

class NameListView(ListView):
    model = Hello
    
class NameDetailView(DetailView):
    model = Hello
    