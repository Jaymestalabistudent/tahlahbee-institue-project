describe('Contact Page Tests', () => {

  beforeEach(() => {
    cy.visit('subpages/contact.html');
  });

  it('should load the contact page and verify the title contains "Contact us"', () => {
    cy.title().should('include', 'Contact us');
  });

  it('should have a visible navbar and header with the correct brand name', () => {
    cy.get('.navbar').should('be.visible');
    cy.get('.navbar-brand').should('exist').and('contain', 'Tahlahbee Institute');
  });

  it('should find the subscription form with an email input and submit button', () => {
    cy.get('input[name="email"]').should('exist');
    cy.get('button[type="submit"]').should('exist');
  });

  it('should have a "Contact Us" heading and a form action attribute', () => {
    cy.get('h2').should('contain', 'Contact Us');
    cy.get('form[action*="formspree"]').should('exist');
  });

  it('should have working social media links', () => {
    cy.get('a[href*="t.me"]').should('exist');
  });

  it('should find the Instagram post embedded on the page', () => {
    cy.get('.instagram-media').should('exist');
  });

  it('should have a visible email input in the contact form', () => {
    cy.get('input#email').should('exist').and('be.visible');
  });

  it('should check the responsiveness of the page on a small screen', () => {
    cy.viewport('iphone-6');
    cy.get('.navbar-toggler').should('be.visible');
  });

});
