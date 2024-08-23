describe('Story Page Tests', () => {
    beforeEach(() => {
      cy.visit('subpages/story.html');
    });
  
    it('should have a title', () => {
      cy.title().should('eq', 'Our stories');
    });
  
    it('should have four modals', () => {
      cy.get('.modal').should('have.length', 4);
    });
  
    it('should have aria labels', () => {
      cy.get('[aria-label]').should('have.length.greaterThan', 0);
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
  