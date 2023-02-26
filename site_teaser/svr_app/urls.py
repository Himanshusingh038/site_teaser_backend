from django.urls import path
from .views import create_announcement
from .views import get_properties
from . import views
from django.views.generic import TemplateView

handler404 = TemplateView.as_view(template_name='404.html')

urlpatterns = [
    path('create-announcement/', create_announcement, name='create_announcement'),
    path('get_properties/', get_properties, name='get_properties'),
    path('add_properties/', views.insert_properties, name='add_properties'),
    path('get_surroundings', views.get_surroundings, name='get_surroundings'),
    path('add_surroundings', views.insert_surrounding, name='add_surroundings'),
    path('send_msg', views.send_msg, name='send_msg'),
]
