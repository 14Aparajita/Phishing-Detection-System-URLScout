// Get the button
let scrollToTopBtn = document.getElementById('scrollToTop');

// Show or hide the button based on scroll position
window.onscroll = function() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        scrollToTopBtn.style.display = 'block';
    } else {
        scrollToTopBtn.style.display = 'none';
    }
};

// Scroll to top function
scrollToTopBtn.onclick = function() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
};

// Scroll to top function
let scrollToTopBtn = document.getElementById('scrollToTop');

scrollToTopBtn.onclick = function() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
};
