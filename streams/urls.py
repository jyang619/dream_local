from django.urls import path

from . import views

app_name = 'streams'

urlpatterns = [
    path('', views.stream, name='stream')
]