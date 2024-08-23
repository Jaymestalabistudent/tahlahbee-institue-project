const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

// Load the HTML file
const html = fs.readFileSync(path.resolve(__dirname, '../about.html'), 'utf8');

let dom;
let document;

describe('About Page', () => {
    beforeAll(() => {
        // Create a new JSDOM instance
        dom = new JSDOM(html, { runScripts: 'dangerously' });
        document = dom.window.document;
    });

    // Test: Check if the preloader exists
    test('pageloader exists', () => {
        const pageloader = document.getElementById('pageloader');
        expect(pageloader).not.toBeNull();
    });

    // Test: Check if the navbar exists and has the correct title
    test('navbar exists and has correct title', () => {
        const navbar = document.querySelector('nav.navbar');
        expect(navbar).not.toBeNull();

        const navbarTitle = document.querySelector('.navbar-title');
        expect(navbarTitle.textContent).toBe('Tahlahbee Institute');
    });

    // Test: Check if all <h2> titles are present and correct
    test('all <h2> titles are correct', () => {
        const expectedTitles = [
            'Early 2022',
            'Mid 2022',
            'Late 2022',
            'Early 2023',
            'Late 2023',
            'Mid 2024'
        ];

        const h2Elements = document.querySelectorAll('h2');
        const h2Texts = Array.from(h2Elements).map(h2 => h2.textContent.trim());

        expectedTitles.forEach(title => {
            expect(h2Texts).toContain(title);
        });
    });

    // Test: Check if the subscription form exists and has the correct aria-labels
    test('subscription form exists with correct aria-labels', () => {
        const form = document.querySelector('[aria-label="Subscription form"]');
        expect(form).not.toBeNull();

        const emailInput = document.querySelector('[aria-label="Email input"]');
        expect(emailInput).not.toBeNull();
        expect(emailInput.type).toBe('email');

        const submitButton = document.querySelector('[aria-label="Subscribe button"]');
        expect(submitButton).not.toBeNull();
        expect(submitButton.type).toBe('submit');
    });

    // Test: Check if the page title is correct
    test('page title is correct', () => {
        const title = document.querySelector('title');
        expect(title.textContent).toBe('About us');
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
});
