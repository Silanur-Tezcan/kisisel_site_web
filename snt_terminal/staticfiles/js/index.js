// Sayfa kaydırıldıkça çalışacak fonksiyon
window.addEventListener('scroll', function() {
    var elements = document.querySelectorAll('.hidden'); // .hidden sınıfına sahip tüm öğeleri seçiyoruz
    elements.forEach(function(element) {
      if (isElementInViewport(element)) { // Öğenin görünür olup olmadığını kontrol ediyoruz
        element.classList.add('visible'); // Eğer görünürse, visible sınıfını ekliyoruz
      }
    });
  });
  
  // Öğenin görünür olup olmadığını kontrol eden fonksiyon
  function isElementInViewport(el) {
    var rect = el.getBoundingClientRect();
    return (
      rect.top < window.innerHeight && rect.bottom > 0
    );
  }
// sertifika card da devam kısmını saklama
document.querySelectorAll('.card').forEach(card => {
  const cardText = card.querySelector('.card-text');
  const scrollTip = card.querySelector('.scroll-tip');

  cardText.addEventListener('mouseenter', () => {
    scrollTip.classList.add('hide');
  });

  cardText.addEventListener('mouseleave', () => {
    scrollTip.classList.remove('hide');
  });
});

  
// sertifika
document.addEventListener('DOMContentLoaded', function () {
  // Swiper.js Konfigürasyonu
  var swiper1 = new Swiper(".mySwiper", {
      slidesPerView: 2,
      spaceBetween: 10,
  
     
      breakpoints: {
          640: { slidesPerView: 2 },
          768: { slidesPerView: 2 },
          1024: { slidesPerView: 4 },
      },
  });

  // Kategori butonları ile içerik filtreleme
  const kategoriButonlari = document.querySelectorAll('.kategori-btn');
  const kurslarContainer = document.getElementById('kurslar-container');

  kategoriButonlari.forEach(button => {
      button.addEventListener('click', function () {
          const kategoriId = this.getAttribute('data-kategori-id');
          
          // Sayfayı kategori parametresiyle yeniden yükle
          window.location.href = `/?kategori=${kategoriId}`;
      });
  });
});
// RESİM BÜYÜTME
function openModal(img) {
  var modal = document.getElementById("imageModal");
  var modalImg = document.getElementById("modalImage");
  modal.style.display = "block";
  modalImg.src = img.src;
}

function closeModal() {
  document.getElementById("imageModal").style.display = "none";
}