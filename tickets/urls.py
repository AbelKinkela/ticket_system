from django.urls import path

from .views import HomePageView, AboutPageView, RequestCreateView, RequestDetailView, RequestUpdateView

urlpatterns = [
    path('request/<int:pk>/edit/', RequestUpdateView.as_view(), name='edit_request'),
    path('request/new/', RequestCreateView.as_view(), name='new_request'), 
    path('request/<int:pk>/', RequestDetailView.as_view(), name='request_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='index'),
]
