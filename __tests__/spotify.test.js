const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const html = fs.readFileSync(path.resolve(__dirname, '../subpages/spotify.html'), 'utf8');

let dom;
let document;

describe('Spotify Page', () => {
    beforeAll(() => {
        dom = new JSDOM(html, { runScripts: "dangerously" });
        document = dom.window.document;
    });

    test('pageloader exists', () => {
        const pageloader = document.getElementById('pageloader');
        expect(pageloader).not.toBeNull();
    });

    test('iframe loads correctly', () => {
        const iframe = document.querySelector('iframe.spotify-embed');
        expect(iframe).not.toBeNull();
        expect(iframe.src).toBe('https://open.spotify.com/embed/episode/2pxdMJSi6l0d0K9DHms7lw?utm_source=generator');
    });

    test('navbar exists and has correct title', () => {
        const navbar = document.querySelector('nav.navbar');
        expect(navbar).not.toBeNull();
        const navbarTitle = document.querySelector('.navbar-title');
        expect(navbarTitle.textContent).toBe('Tahlahbee Institute');
    });

    test('page title is correct', () => {
        const title = document.querySelector('title');
        expect(title.textContent).toBe('Spotify');
    });

    test('metadata is correct', () => {
        const metaDescription = document.querySelector('meta[name="description"]');
        expect(metaDescription.content).toBe('Tahlahbee Institute is a dedicated self-help website for single fathers, offering a wide range of eBooks, advice courses, and inspirational quotes to support and empower single dads on their journey');

        const metaKeywords = document.querySelector('meta[name="keywords"]');
        expect(metaKeywords.content).toBe('single fathers, self-help, eBooks, advice courses, inspirational quotes, single dads, parenting, fatherhood, support for fathers, empowerment for dads');
    });

   

    // New test: Check for the presence of a footer element
    test('footer exists', () => {
        const footer = document.querySelector('footer');
        expect(footer).not.toBeNull();
    });
});