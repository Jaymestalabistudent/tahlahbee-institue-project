const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

describe('Page Tests', () => {
  let dom;
  let document;
  let window;

  beforeAll(() => {
    // Load the HTML file into a DOM object
    const html = fs.readFileSync(path.resolve(__dirname, '../subpages/story.html'), 'utf8');
    dom = new JSDOM(html, { runScripts: 'dangerously', resources: 'usable' });
    document = dom.window.document;
    window = dom.window;
  });

  test('should open Matt modal on button click', () => {
    const button = document.querySelector('button[data-bs-toggle="modal"]');
    button.click();
    
    const modalTitle = document.querySelector('#modal1 .modal-title').textContent;
    expect(modalTitle).toBe('Matt : Separated');
  });

  test('should render Matt image', () => {
    const imageSrc = document.querySelector('img[alt="matt"]').getAttribute('src');
    expect(imageSrc).toContain('matt.jpg');
  });

  test('should open Dean modal on button click', () => {
    const button = document.querySelector('button[data-bs-toggle="modal"]');
    button.click();
    
    const modalTitle = document.querySelector('#modal2 .modal-title').textContent;
    expect(modalTitle).toBe('Dean : Divorced');
  });

  test('should render Dean image', () => {
    const imageSrc = document.querySelector('img[alt="dean"]').getAttribute('src');
    expect(imageSrc).toContain('dean.jpg');
  });

  test('should open Joe modal on button click', () => {
    const button = document.querySelector('button[data-bs-toggle="modal"]');
    button.click();
    
    const modalTitle = document.querySelector('#modal3 .modal-title').textContent;
    expect(modalTitle).toBe('Joe : Ex-offender');
  });

  test('should render Joe image', () => {
    const imageSrc = document.querySelector('img[alt="joe"]').getAttribute('src');
    expect(imageSrc).toContain('joe.jpg');
  });

  test('should open Miller modal on button click', () => {
    const button = document.querySelector('button[data-bs-toggle="modal"]');
    button.click();
    
    const modalTitle = document.querySelector('#modal4 .modal-title').textContent;
    expect(modalTitle).toBe('Miller : Depression');
  });

  test('should render Miller image', () => {
    const imageSrc = document.querySelector('img[alt="miller"]').getAttribute('src');
    expect(imageSrc).toContain('mill.jpg');
  });

  test('should include favicon links', () => {
    const favicons = document.querySelectorAll('link[rel="icon"]');
    expect(favicons.length).toBeGreaterThan(0);
  });

  test('should have correct meta description', () => {
    const metaDescription = document.querySelector('meta[name="description"]').getAttribute('content');
    expect(metaDescription).toBe(
      'Tahlahbee Institute is a dedicated self-help website for single fathers, offering a wide range of eBooks, advice courses, and inspirational quotes to support and empower single dads on their journey'
    );
  });
});
