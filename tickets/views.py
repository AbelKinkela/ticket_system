from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Request, Ticket, Comments

# Create your views here.

class HomePageView(ListView):
    model=Request
    template_name = 'index.html'
    context_object_name = 'all_requests_list' # new


class AboutPageView(TemplateView):
    template_name = 'about.html'