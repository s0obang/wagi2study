from django.contrib import admin
from django.urls import path
from .views import wrtie,main,detail
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('', main, name='main'),
    path('write/', wrtie, name='write'),
    path('<int:post_id>/', detail, name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)