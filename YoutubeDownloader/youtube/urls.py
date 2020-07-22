from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.home,name='home_page'),
    path('download-ready/',views.download_ready,name='download_ready'),
    path('test-celery/<int:num1>/<int:num2>/',views.test_celery,name='test_celery'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


