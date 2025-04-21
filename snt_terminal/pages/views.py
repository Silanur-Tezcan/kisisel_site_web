from django.shortcuts import render,redirect
from .models import Sertifika, Category,Projeler
from pages.models import Mesaj,Hakkimda
from django.core.paginator import Paginator

def anasayfa(request):
    kategori_id = request.GET.get('kategori')  # Kategori ID'si URL parametresiyle geliyor
    kategoriler = Category.objects.all()
    hakkimda = Hakkimda.objects.first()

    if kategori_id:
        sertifikalar = Sertifika.objects.filter(kategori__id=kategori_id)
    else:
        sertifikalar = Sertifika.objects.all()

    projeler = Projeler.objects.all()  # Projeler filtresiz kalsın

    return render(request, 'pages/anasayfa.html', {
        'sertifikalar': sertifikalar,
        'projeler': projeler,
        'kategoriler': kategoriler,
        'hakkimda':hakkimda,
    })

def proje(request):
    projeler = Projeler.objects.all()
    return render(request, 'pages/proje.html', {'projeler': projeler})

def iletisim(request):
    mesaj_gonderildi = False

    if request.method == 'POST':
        ad_soyad = request.POST.get('ad_soyad')
        email = request.POST.get('email')
        konu = request.POST.get('konu')
        mesaj = request.POST.get('mesaj')

        Mesaj.objects.create(
            ad_soyad=ad_soyad,
            email=email,
            konu=konu,
            mesaj=mesaj
        )

        mesaj_gonderildi = True

    return render(request, 'pages/iletisim.html', {'mesaj_gonderildi': mesaj_gonderildi})
def search(request):
    query = request.GET.get('q', '')  # Arama sorgusunu al
    projeler_list = Projeler.objects.filter(baslik__icontains=query)  # Başlıkta arama yap
    sertifikalar_list = Sertifika.objects.filter(baslik__icontains=query)  # Sertifikalar için de aynı işlem yapılabilir.

    # Sayfalama işlemleri
    paginator_proje = Paginator(projeler_list, 5)  # 5 proje her sayfada gösterilecek
    paginator_sertifika = Paginator(sertifikalar_list, 5)  # 5 sertifika her sayfada gösterilecek

    # Sayfa numaralarını al
    page_proje = request.GET.get('page_proje')  # Projeler için sayfa numarasını al
    page_sertifika = request.GET.get('page_sertifika')  # Sertifikalar için sayfa numarasını al

    # Sayfalandırılmış projeler ve sertifikalar
    projeler = paginator_proje.get_page(page_proje)
    sertifikalar = paginator_sertifika.get_page(page_sertifika)

    return render(request, 'partials/_search.html', {
        'projeler': projeler,
        'sertifikalar': sertifikalar,
        'query': query,
    })

def arama_sonuc(request):
    query = request.GET.get('q')  # Arama sorgusu

    # Proje verilerini çekme
    projeler_list = Projeler.objects.all()  # Bu, arama kriterlerine göre filtrelenebilir
    sertifikalar_list = Sertifika.objects.all()  # Aynı şekilde sertifikalar için de yapılabilir

    # Sayfalama
    paginator_proje = Paginator(projeler_list, 5)  # 5 proje her sayfada gösterilecek
    paginator_sertifika = Paginator(sertifikalar_list, 5)  # 5 sertifika her sayfada gösterilecek

    # Sayfa numarasını al
    page_proje = request.GET.get('page')  # Projeler için sayfa numarasını al
    page_sertifika = request.GET.get('page')  # Sertifikalar için sayfa numarasını al

    # Sayfalandırılmış projeleri ve sertifikaları al
    projeler = paginator_proje.get_page(page_proje)
    sertifikalar = paginator_sertifika.get_page(page_sertifika)

    return render(request, 'arama_sonuc.html', {
        'projeler': projeler,
        'sertifikalar': sertifikalar,
        'query': query,
    })