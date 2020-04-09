from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Request, Ticket, Comments

# Create your views here.

class HomePageView(ListView):
    model=Request
    template_name = 'index.html'
    context_object_name = 'all_requests_list' # new


class AboutPageView(TemplateView):
    template_name = 'about.html'

class RequestCreateView(CreateView):
    model = Request
    template_name = 'new_request.html'
    fields = '__all__'
    def form_valid(self, form): 
        form.instance.user = self.request.user
        return super().form_valid(form)

class RequestDetailView(DetailView):
    model = Request
    template_name = 'request_detail.html'
    

class RequestUpdateView(UpdateView):
    model = Request
    template_name = 'edit_request.html'
    fields = '__all__'