// アニメーション（fade-in）
document.addEventListener('DOMContentLoaded', function () {
  const fadeElements = document.querySelectorAll('.fade-in');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, {
    threshold: 0.1
  });
  fadeElements.forEach(element => {
    observer.observe(element);
  });
});

// モーダル制御（予約）
document.addEventListener('DOMContentLoaded', function () {
  const modal = document.getElementById('reservationModal');
  const openButton = document.getElementById('reservationButton');
  const closeButton = document.getElementById('closeModal');
  const reservationButtons = document.querySelectorAll('.bg-secondary');

  function openModal() {
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }

  openButton.addEventListener('click', openModal);
  reservationButtons.forEach(button => {
    button.addEventListener('click', openModal);
  });
  closeButton.addEventListener('click', closeModal);

  modal.addEventListener('click', function (e) {
    if (e.target === modal) {
      closeModal();
    }
  });
})