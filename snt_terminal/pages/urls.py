from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('proje/', views.proje, name='proje'),
    path('iletisim/', views.iletisim, name='iletisim'),

    path('search/', views.search, name='search'),  # Arama URL'i
    
]

# Geliştirme ortamı için media ve static dosyaları
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # <--- BU EKLENDİ
