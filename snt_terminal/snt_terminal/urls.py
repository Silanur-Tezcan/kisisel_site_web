from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),  # varsa başka app’lerinizin urls.py’sini de ekleyin
    path('', include('pages.urls')),  # ana sayfayı yönlendirmek için
]

# Static ve Media dosyaları ayarları
if settings.DEBUG:  # Sadece DEBUG modunda çalışır
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)