const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

// Load the HTML file
const html = fs.readFileSync(path.resolve(__dirname, '../quicklinks.html'), 'utf8');

let dom;
let document;

describe('Links Page', () => {
    beforeAll(() => {
        // Create a new JSDOM instance
        dom = new JSDOM(html, { runScripts: 'dangerously' });
        document = dom.window.document;
    });

    // Test: Check if the preloader exists and has the correct structure
    test('pageloader exists and structure is correct', () => {
        const pageloader = document.getElementById('pageloader');
        expect(pageloader).not.toBeNull();

        const spinner = pageloader.querySelector('.spinner');
        expect(spinner).not.toBeNull();
        
        const bounceElements = spinner.querySelectorAll('.bounce1, .bounce2, .bounce3');
        expect(bounceElements.length).toBe(3);
    });

    // Test: Check if the navbar exists and contains the correct elements
    test('navbar exists and has correct structure', () => {
        const navbar = document.querySelector('nav.navbar');
        expect(navbar).not.toBeNull();

        const navbarBrand = navbar.querySelector('.navbar-brand');
        expect(navbarBrand).not.toBeNull();

        const logo = navbarBrand.querySelector('img.navbar-logo');
        expect(logo).not.toBeNull();
        expect(logo.getAttribute('src')).toBe('assets/img/logo/logo.png');

        const navbarTitle = navbarBrand.querySelector('.navbar-title');
        expect(navbarTitle).not.toBeNull();
        expect(navbarTitle.textContent).toBe('Tahlahbee Institute');
    });

    // Test: Check if all Lottie files are loading correctly
    test('Lottie files are loading', () => {
        const lottiePlayers = document.querySelectorAll('dotlottie-player');
        expect(lottiePlayers.length).toBeGreaterThan(0);

        lottiePlayers.forEach(player => {
            const src = player.getAttribute('src');
            expect(src).toMatch(/https:\/\/lottie\.host\/.+\.json/);
        });
    });

    // Test: Check if all buttons are present and correctly labeled
    test('all buttons exist and have correct labels', () => {
        const buttons = document.querySelectorAll('button.btn-custom');
        expect(buttons.length).toBeGreaterThan(0);

        buttons.forEach(button => {
            expect(button.textContent.trim()).not.toBe('');
            expect(button.classList.contains('btn-dark')).toBe(true);
        });
    });

    // Test: Check if all <h2> titles are present and correct
    test('all <h2> titles are correct', () => {
        const expectedTitles = [
            'Members Zone',
            'The Numbers',
            'Meal Menu',
            'Thoughts',
            'Our stories',
            'Mental Health',
            'Spotify',
            'User Quote',
            'Contact us'
        ];

        const h2Elements = document.querySelectorAll('h2.quick-title');
        const h2Texts = Array.from(h2Elements).map(h2 => h2.textContent.trim());

        expectedTitles.forEach(title => {
            expect(h2Texts).toContain(title);
        });
    });

    // Test: Check if the page title is correct
    test('page title is correct', () => {
        const title = document.querySelector('title');
        expect(title.textContent).toBe('Links');
    });

    // Test: Check if metadata is correct
    test('metadata is correct', () => {
        const metaDescription = document.querySelector('meta[name="description"]');
        expect(metaDescription).not.toBeNull();
        expect(metaDescription.content.trim()).toBe('Tahlahbee Institute is a dedicated self-help website for single fathers, offering a wide range of eBooks, advice courses, and inspirational quotes to support and empower single dads on their journey');

        const metaKeywords = document.querySelector('meta[name="keywords"]');
        expect(metaKeywords).not.toBeNull();
        expect(metaKeywords.content.trim()).toBe('single fathers, self-help, eBooks, advice courses, inspirational quotes, single dads, parenting, fatherhood, support for fathers, empowerment for dads');
    });

    // Test: Check if all images in the quick sections have alt attributes
    test('all images in quick sections have alt attributes', () => {
        const images = document.querySelectorAll('.quick-image img');
        images.forEach(img => {
            expect(img.hasAttribute('alt')).toBe(true);
            expect(img.getAttribute('alt').trim()).not.toBe('');
        });
    });

    // Test: Check if the footer exists and contains the copyright notice
    test('footer exists and contains copyright notice', () => {
        const footer = document.querySelector('footer.footer');
        expect(footer).not.toBeNull();

        const copyright = footer.querySelector('small');
        expect(copyright).not.toBeNull();
        expect(copyright.textContent).toContain('Copyright');
    });
});
