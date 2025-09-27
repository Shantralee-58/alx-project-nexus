from django.urls import path
from . import views

# This is necessary for namespacing and linking in templates
app_name = 'stores' 

urlpatterns = [
    # path is just '' because the main sustainify/urls.py handles the 'stores/' part
    path('', views.store_list_view, name='store_list'),
]
