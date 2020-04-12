from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home_page'),
    path('download-ready/',views.download_ready,name='download_ready'),
    path('download/',views.download,name='download'),
]
