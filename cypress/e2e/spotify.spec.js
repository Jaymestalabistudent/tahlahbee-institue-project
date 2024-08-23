describe('Spotify Page Tests', () => {
    beforeEach(() => {
      cy.visit('subpages/spotify.html');
    });
  
    it('should have a title', () => {
      cy.title().should('eq', 'Spotify');
    });
  
    it('should have aria labels', () => {
      cy.get('[aria-label]').should('have.length.greaterThan', 0);
    });
 
    it('should have a functional Spotify iframe', () => {
      cy.get('iframe[src*="spotify"]').should('exist').and('be.visible');
    });
  
    it('should have a navigation bar', () => {
      cy.get('nav').should('exist');
    });
  
    it('should have functional navigation links', () => {
      cy.get('nav a').each(($el) => {
        cy.wrap($el).should('have.attr', 'href').and('not.be.empty');
      });
    });
 
  });
  