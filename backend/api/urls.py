from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('boolean/', views.boolean, name='boolean'),
    path('vect/', views.boolean, name='Vectorial')
]