document.addEventListener('DOMContentLoaded', () => {
    // Validate contact form on submit
    const contactForm = document.querySelector('form');
    console.log('Contact Form:', contactForm); // Check if the form is found

    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();
            console.log("Script is working!"); // Confirm the script is running

            if (!name || !email || !message) {
                alert('Please fill in all required fields.');
                event.preventDefault();  // Prevent form submission
            } else if (!validateEmail(email)) {
                alert('Please enter a valid email address.');
                event.preventDefault();  // Prevent form submission
            } else {
                console.log("Form submitted successfully!");  // Log successful submission
                contactForm.reset(); // Clear the form fields
                // If needed, you could also submit the form via AJAX here
            }
        });
    } else {
        console.error('Contact form not found!'); // Log error if form is not found
    }

    // Email validation function
    function validateEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    // Scroll to sections when navbar links are clicked
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            const target = e.target.getAttribute('href').substring(1);
            const section = document.getElementById(target);
            if (section) {
                section.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});
