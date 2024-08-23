describe('About Page Tests', () => {
    beforeEach(() => {
      cy.visit('about.html');
    });
  
    it('should have a title', () => {
      cy.title().should('eq', 'About us');
    });
  
    it('should have a preloader', () => {
      cy.get('#pageloader').should('exist');
    });
  
    it('should have aria labels', () => {
      cy.get('[aria-label]').should('have.length.greaterThan', 0);
    });
  
    it('should have a main content section', () => {
      cy.get('main').should('exist');
    });
  
    it('should display the timeline correctly', () => {
      cy.get('.time-container').should('have.length.greaterThan', 0);
    });
  
  
    // Additional Tests
    it('should have a navigation bar', () => {
      cy.get('nav').should('exist');
    });
  
    it('should have functional navigation links', () => {
      cy.get('nav a').each(($el) => {
        cy.wrap($el).should('have.attr', 'href').and('not.be.empty');
      });
    });
  
  });
  