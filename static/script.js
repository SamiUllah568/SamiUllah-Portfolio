window.addEventListener('scroll', function() {
    const header = document.getElementById('header');
    if (window.scrollY > 0) {
      header.style.backgroundColor = 'transparent';
    }
  });
  