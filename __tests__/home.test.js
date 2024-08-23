const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

// Load the HTML file
const html = fs.readFileSync(path.resolve(__dirname, '../index.html'), 'utf8');

let dom;
let document;

describe('Home Page', () => {
    beforeAll(() => {
        // Create a new JSDOM instance
        dom = new JSDOM(html, { runScripts: 'dangerously' });
        document = dom.window.document;
    });

    // Test: Check if the preloader exists
    test('preloader exists', () => {
        const preloader = document.getElementById('overlay');
        expect(preloader).not.toBeNull();
    });

    // Test: Check if the navbar exists and has the correct title
    test('navbar exists and has correct title', () => {
        const navbar = document.querySelector('nav.navbar');
        expect(navbar).not.toBeNull();

        const navbarTitle = document.querySelector('.navbar-title');
        expect(navbarTitle.textContent.trim()).toBe('Tahlahbee Institute');
    });

    // Test: Check if all <h1> headings are present and correct
    test('heading contains correct text', () => {
        const heading = document.querySelector('.caption h1');
        expect(heading).not.toBeNull();
        expect(heading.textContent).toMatch(/I'm a\|/);
    });

    // Test: Check if the slider contains the correct number of slides
    test('slider has the correct number of slides', () => {
        const slides = document.querySelectorAll('.blog-slider__item');
        expect(slides.length).toBe(6);
    });



    // Test: Check if the page title is correct
    test('page title is correct', () => {
        const title = document.querySelector('title');
        expect(title.textContent).toBe('Tahlahbee Institute');
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

    // Test: Check if the font-awesome script is included
    test('font-awesome script is included', () => {
        const scripts = Array.from(document.querySelectorAll('script'));
        const fontAwesomeScript = scripts.find(script =>
            script.src.includes('kit.fontawesome.com')
        );
        expect(fontAwesomeScript).toBeDefined();
    });
});
