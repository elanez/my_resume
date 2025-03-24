// Select all sections
const sections = document.querySelectorAll('section');

// Create Intersection Observer
const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
    if (entry.isIntersecting) {
        entry.target.classList.add('active');
        // Optional: Stop observing after animation triggers
        observer.unobserve(entry.target);
    }
    });
}, {
    threshold: 0.3 // Trigger when 30% of the section is visible
});

// Observe each section
sections.forEach(section => {
    observer.observe(section);
});