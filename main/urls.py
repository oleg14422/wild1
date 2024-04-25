from django.urls import path
from . import views


urlpatterns = [
    path('', views.wildPage, name='wild'),
    path('cooler_page', views.wildPage2, name='wild2')
]