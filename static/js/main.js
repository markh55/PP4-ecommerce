//success and error messages fade out after 4 seconds//
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        const alerts = document.querySelectorAll('.message-container .alert');
        alerts.forEach(alert => {
            alert.classList.remove('show');
            alert.classList.add('fade');
            setTimeout(() => alert.remove(), 500);
        });
    }, 4000);
});

// this code was taken from perosonal project and modified to fit the needs of this project//
// Add fade-in and slide-in animations to elements when they enter the viewport
document.addEventListener('DOMContentLoaded', function() {
  const elements = document.querySelectorAll(".fade-in, .fade-in-left, .fade-left, .fade-in-right");
  
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  elements.forEach(element => {
    observer.observe(element);
  });
});