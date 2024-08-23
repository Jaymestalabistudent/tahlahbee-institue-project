const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const html = fs.readFileSync(path.resolve(__dirname, '../books.html'), 'utf8');

let dom;
let document;

describe('Bookshop Page', () => {
    beforeAll(() => {
        dom = new JSDOM(html, { runScripts: "dangerously" });
        document = dom.window.document;
    });

    test('page title is correct', () => {
        const title = document.querySelector('title');
        expect(title.textContent).toBe('Bookshop');
    });

    test('meta tags are correct', () => {
        const metaDescription = document.querySelector('meta[name="description"]');
        expect(metaDescription).not.toBeNull();
        expect(metaDescription.content.trim()).toBe('Tahlahbee Institute is a dedicated self-help website for single fathers, offering a wide range of eBooks, advice courses, and inspirational quotes to support and empower single dads on their journey');

        const metaKeywords = document.querySelector('meta[name="keywords"]');
        expect(metaKeywords).not.toBeNull();
        expect(metaKeywords.content.trim()).toBe('single fathers, self-help, eBooks, advice courses, inspirational quotes, single dads, parenting, fatherhood, support for fathers, empowerment for dads');
    });

    test('navbar exists and has correct title', () => {
        const navbar = document.querySelector('nav.navbar');
        expect(navbar).not.toBeNull();
        const navbarTitle = document.querySelector('.navbar-title');
        expect(navbarTitle.textContent).toBe('Tahlahbee Institute');
    });

    test('preloader exists', () => {
        const preloader = document.getElementById('pageloader');
        expect(preloader).not.toBeNull();
    });

    test('main content headings are correct', () => {
        const mainHeading = document.querySelector('h1');
        expect(mainHeading.textContent).toBe('Bookstore');
        const subHeading = document.querySelector('p');
        expect(subHeading.textContent).toBe('Download Books and Increase Your Knowledge');
    });

    test('cards are present with correct content', () => {
        const cardTitles = [
            'Food : A Guide',
            'Meditation : A Journey',
            'Fitness 4 U',
            'Stress Free',
            '5 Steps',
            'Developing Courage'
        ];

        const cardElements = document.querySelectorAll('.card');
        expect(cardElements.length).toBe(6);

        cardTitles.forEach(title => {
            const cardTitleElement = Array.from(cardElements).find(card => card.querySelector('.card-title').textContent.includes(title));
            expect(cardTitleElement).not.toBeNull();
        });
    });

    test('download links are correct', () => {
        const downloadLinks = [
            'https://drive.google.com/uc?export=download&id=1-0_KzROmxL4rtFn35z0WSnsY1d3bin57',
            'https://drive.google.com/uc?export=download&id=1-3CRVcE0_CoDImc0lRNAtuxYkdctfZwV',
            'https://drive.google.com/uc?export=download&id=1-poM9P3ZP1mnRxt5r9ZIWIkeGmLdSyS1',
            'https://drive.google.com/uc?export=download&id=1-kZNh-xklK1aJ5mVq6lkcUlLZCIhVVNZ',
            'https://drive.google.com/uc?export=download&id=1-_s0cN9V8qZ4mc2HoL245h_YlmnSmORJ',
            'https://drive.google.com/uc?export=download&id=1-G-RcHD6pYzHLl94O-_M75KzAKk6xfFn'
        ];

        const linkElements = document.querySelectorAll('a.btn-custom');
        expect(linkElements.length).toBe(6);

        linkElements.forEach((link, index) => {
            expect(link.href).toBe(downloadLinks[index]);
        });
    });
});
