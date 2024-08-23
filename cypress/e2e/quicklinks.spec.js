
describe('Links Page Tests', () => {
  beforeEach(() => {
    cy.visit('quicklinks.html');
  });

  it('should have the correct title', () => {
    cy.title().should('eq', 'Links');
  });

  it('should have a navigation bar', () => {
    cy.get('header.u-header').should('exist');
    cy.get('nav.navbar').should('exist');
  });

  it('should have functional navigation links', () => {
    cy.get('nav.navbar').within(() => {
      cy.get('a.nav-link[href="home.html"]').should('exist').and('have.text', 'Home');
      cy.get('a.nav-link[href="books.html"]').should('exist').and('have.text', 'Books');
      cy.get('a.nav-link[href="about.html"]').should('exist').and('have.text', 'About');
      cy.get('a.nav-link[href="subpages/contact.html"]').should('exist').and('have.text', 'Contact');
    });
  });

  it('should display the preloader', () => {
    cy.get('#pageloader').should('be.visible');
    cy.get('#pageloader .spinner').should('exist');
  });

  it('should have a Sign-in button that redirects to the correct URL', () => {
    cy.get('button.btn-custom').contains('Sign-in').should('exist').and('have.attr', 'onclick', "window.location.href='https://tahlahbee-institute-project.onrender.com/register'");
  });

  it('should have a Recipes button that redirects to the correct URL', () => {
    cy.get('button.btn-custom').contains('Recipes').should('exist').and('have.attr', 'onclick', "window.location.href='subpages/recipe.html'");
  });

  it('should have a Get help button that redirects to the correct URL', () => {
    cy.get('button.btn-custom').contains('Get help').should('exist').and('have.attr', 'onclick', "window.location.href='subpages/mental.html'");
  });

  it('should have a Spotify button that redirects to the correct URL', () => {
    cy.get('button.btn-custom').contains('Spotify').should('exist').and('have.attr', 'onclick', "window.location.href='subpages/spotify.html'");
  });

  it('should have a Contact us button that redirects to the correct URL', () => {
    cy.get('button.btn-custom').contains('Contact us').should('exist').and('have.attr', 'onclick', "window.location.href='subpages/contact.html'");
  });
});
