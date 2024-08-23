const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

describe('Mental Health Page', () => {
  let dom;
  let document;
  let window;

  beforeAll(() => {
    // Load the HTML file into a DOM object
    const filePath = path.join(__dirname, '../subpages/mental.html');
    const html = fs.readFileSync(filePath, 'utf8');
    dom = new JSDOM(html, { runScripts: 'dangerously', resources: 'usable' });
    document = dom.window.document;
    window = dom.window;
  });

  test('should have correct title', () => {
    expect(document.title).toBe('Mental Health');
  });

  test('should have correct meta description', () => {
    const metaDescription = document.querySelector('meta[name="description"]').getAttribute('content').trim();
    expect(metaDescription).toBe('Tahlahbee Institute is a dedicated self-help website for single fathers, offering a wide range of eBooks, advice courses, and inspirational quotes to support and empower single dads on their journey');
  });

  test('should have a navbar', () => {
    const navbar = document.querySelector('nav.navbar');
    expect(navbar).not.toBeNull();
  });

  test('should have links that open in a new tab', () => {
    const links = Array.from(document.querySelectorAll('a[target="_blank"]')).map(link => link.href);
    expect(links.length).toBeGreaterThan(0); // Ensure there are links with target="_blank"
    expect(links).toContain('https://www.psychologytoday.com/gb');
    expect(links).toContain('https://www.thecalmzone.net/');
    expect(links).toContain('https://andysmanclub.co.uk/');
  });

  test('should have a preloader', () => {
    const preloader = document.querySelector('#pageloader');
    expect(preloader).not.toBeNull();
  });
});
