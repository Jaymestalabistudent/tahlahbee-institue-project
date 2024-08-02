
// Wait until the DOM is fully loaded and parsed
document.addEventListener('DOMContentLoaded', function() {
    console.log('Document is fully loaded and parsed');

    // Check if the navbar element is present
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        console.log('Navbar is present');
    } else {
        console.log('Navbar is missing');
    }

    // Check if the preloader element is present
    const preloader = document.getElementById('pageloader');
    if (preloader) {
        console.log('Preloader is present');
    } else {
        console.log('Preloader is missing');
    }

    // Check if the blog slider element is present
    const blogSlider = document.querySelector('.blog-slider');
    if (blogSlider) {
        console.log('Blog slider is present');
    } else {
        console.log('Blog slider is missing');
    }

    // Check if any modals are present
    const modals = document.querySelectorAll('[uk-modal]');
    if (modals.length > 0) {
        console.log(`Found ${modals.length} modals`);
    } else {
        console.log('No modals found');
    }

    // Check if any dotlottie-player elements are present
    const lottiePlayers = document.querySelectorAll('dotlottie-player');
    if (lottiePlayers.length > 0) {
        console.log(`Found ${lottiePlayers.length} dotlottie-player elements`);
    } else {
        console.log('No dotlottie-player elements found');
    }
});
