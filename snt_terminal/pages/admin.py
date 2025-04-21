from django.contrib import admin
from .models import Sertifika, Projeler, Category, ProjeResmi,Hakkimda


class ProjeResmiInline(admin.TabularInline):
    model = ProjeResmi
    extra = 8 # Varsayılan olarak 1 resim ekleme alanı sağlar

class ProjelerAdmin(admin.ModelAdmin):
    inlines = [ProjeResmiInline]
    def resim_sayisi(self, obj):
        return obj.proje_resimleri.count()  # İlgili projeye ait resim sayısını döndürür.
    resim_sayisi.short_description = 'Resim Sayısı'  # Kolon başlığını değiştirmek için

    list_display = ('baslik', 'resim_sayisi')  # 'resim_sayisi' fonksiyonunu listele
class SertifikaAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'kategori') 
    list_filter = ('kategori',)


admin.site.register(Projeler, ProjelerAdmin)

admin.site.register(Sertifika,SertifikaAdmin)

admin.site.register(Category)

admin.site.register(Hakkimda)