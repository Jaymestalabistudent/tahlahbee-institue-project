const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const html = fs.readFileSync(path.resolve(__dirname, '../subpages/contact.html'), 'utf8');
let dom;
let document;

describe('Contact Page', () => {
  beforeAll(() => {
	dom = new JSDOM(html);
	document = dom.window.document;
  });

  test('Page title should be "Contact us"', () => {
	const title = document.querySelector('title').textContent;
	expect(title).toBe('Contact us');
  });

  test('Meta description should be correct', () => {
	const metaDescription = document.querySelector('meta[name="description"]').getAttribute('content').trim();
	expect(metaDescription).toBe('Tahlahbee Institute is a dedicated self-help website for single fathers, offering a wide range of eBooks, advice courses, and inspirational quotes to support and empower single dads on their journey');
  });

  test('Navigation bar should contain a "Back" link', () => {
	const navLink = document.querySelector('nav .nav-link').textContent;
	expect(navLink).toBe('Back');
  });

  test('Subscription form should exist and have the correct action URL', () => {
	const form = document.querySelector('#subscription-form');
	expect(form).not.toBeNull();
	expect(form.getAttribute('action')).toBe('https://formsubmit.co/tahlahbee.institute@gmail.com');
  });

  test('Preloader should exist', () => {
	const preloader = document.querySelector('#pageloader');
	expect(preloader).not.toBeNull();
  });
});