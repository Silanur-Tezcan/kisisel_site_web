from django.db import models
class Category(models.Model):
    kategori=models.CharField(max_length=100)

    def __str__(self):
        return self.kategori

class Sertifika(models.Model):
    baslik = models.CharField(max_length=100)
    aciklama = models.TextField(blank=True)
    resim = models.ImageField(upload_to='sertifikalar/')
    kategori = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.baslik

# projeler/models.py

class Projeler(models.Model):
    baslik = models.CharField(max_length=100)
    aciklama = models.TextField(blank=True)
    resim = models.ImageField(upload_to='projeler/')
    video = models.FileField(upload_to='projeler/videolar/', blank=True, null=True)  # Yeni eklendi
    site_link = models.URLField(blank=True, null=True)  # Yeni eklendi

    def __str__(self):
        return self.baslik

class ProjeResmi(models.Model):
    proje = models.ForeignKey('Projeler', related_name='proje_resimleri', on_delete=models.CASCADE)
    resim = models.ImageField(upload_to='projeler/resimler/')

    def __str__(self):
        return f"Resim for {self.proje.baslik}"
class Mesaj(models.Model):
    ad_soyad = models.CharField(max_length=100)
    email = models.EmailField()
    konu = models.CharField(max_length=200)
    mesaj = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ad_soyad} - {self.konu}"

class Hakkimda(models.Model):
    baslik = models.CharField(max_length=200, default="SILA NUR TEZCAN")
    aciklama = models.TextField()
    cv_pdf = models.FileField(upload_to='cv_dosyalar/', blank=True, null=True)

    def __str__(self):
        return self.baslik