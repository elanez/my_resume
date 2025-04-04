document.addEventListener('DOMContentLoaded', () => {
    // Select all sections and elements marked for animation
    const elementsToAnimate = document.querySelectorAll('section, .animate-section');

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
        threshold: 0.2 // Trigger when 20% of the element is visible (adjust as needed)
    });

    // Observe each element
    elementsToAnimate.forEach(element => {
        observer.observe(element);
    });
});