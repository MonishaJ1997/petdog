const slider = document.getElementById('slider');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

let currentIndex = 0;
const totalItems = document.querySelectorAll('.card').length;
let itemsPerPage = getItemsPerPage();

function getItemsPerPage() {
  if (window.innerWidth <= 480) return 1;
  if (window.innerWidth <= 768) return 2;
  if (window.innerWidth <= 1024) return 3;
  return 5;
}

function updateSlider() {
  itemsPerPage = getItemsPerPage();
  const offset = -(currentIndex * (100 / itemsPerPage));
  slider.style.transform = `translateX(${offset}%)`;

  prevBtn.classList.toggle('hidden', currentIndex === 0);
  nextBtn.classList.toggle('hidden', currentIndex >= totalItems - itemsPerPage);
}

nextBtn.addEventListener('click', () => {
  if (currentIndex < totalItems - itemsPerPage) {
    currentIndex++;
    updateSlider();
  }
});

prevBtn.addEventListener('click', () => {
  if (currentIndex > 0) {
    currentIndex--;
    updateSlider();
  }
});

window.addEventListener('resize', updateSlider);

updateSlider();
