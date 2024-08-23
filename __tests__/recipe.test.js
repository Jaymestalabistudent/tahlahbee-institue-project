const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

describe('Recipe Page', () => {
  let dom;
  let document;

  beforeAll(() => {
    // Load the HTML file into a DOM object
    const html = fs.readFileSync(path.resolve(__dirname, '../subpages/recipe.html'), 'utf8');
    dom = new JSDOM(html, { runScripts: "dangerously" });
    document = dom.window.document;
  });

  test('should have correct title', () => {
    const title = document.title;
    expect(title).toBe('Recipes');
  });

  test('should have correct meta description', () => {
    const metaDescription = document.querySelector('meta[name="description"]').getAttribute('content').trim();
    expect(metaDescription).toBe('Tahlahbee Institute is a dedicated self-help website for single fathers, offering a wide range of eBooks, advice courses, and inspirational quotes to support and empower single dads on their journey');
  });

  test('should have correct recipe placeholder', () => {
    const placeholder = document.querySelector('#recipe-app-user-inp').getAttribute('placeholder');
    expect(placeholder).toBe('Type A Dish Name Here..');
  });

  test('should have recipe-app-header', () => {
    const header = document.querySelector('.recipe-app-header h1').textContent.trim();
    expect(header).toBe('Recipe App');
  });

  test('should have a navbar', () => {
    const navbar = document.querySelector('nav.navbar');
    expect(navbar).not.toBeNull();
  });
});
