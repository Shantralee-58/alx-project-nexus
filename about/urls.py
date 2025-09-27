from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about_us_view, name='about_us'),
    path('contact/', views.contact_us_view, name='contact_us'),
]

