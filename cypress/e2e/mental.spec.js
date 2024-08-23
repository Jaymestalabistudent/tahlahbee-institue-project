describe('Mental Health Page Tests', () => {

  beforeEach(() => {
    // Visit the page before each test
    cy.visit('subpages/mental.html'); 
  });

  it('should load the page and verify the title is "Mental Health"', () => {
    cy.title().should('eq', 'Mental Health');
  });

  it('should have a visible navbar with a logo and title', () => {
    cy.get('.navbar').should('be.visible');
    cy.get('.navbar-logo').should('have.attr', 'src', '../assets/img/logo/logo.png');
    cy.get('.navbar-title').should('contain', 'Tahlahbee Institute');
  });

  it('should have a preloader element and ensure it is hidden after load', () => {
    cy.get('#pageloader').should('exist');
  });

  it('should display the main heading with animated words', () => {
    cy.get('.cd-headline').should('be.visible').and('contain', "I'm |");
    cy.get('.cd-words-wrapper b').should('have.length', 6);
  });

  it('should have working links with correct targets', () => {
    cy.get('a[href="https://www.psychologytoday.com/gb"]').should('have.attr', 'target', '_blank');
    cy.get('a[href="https://www.thecalmzone.net/"]').should('have.attr', 'target', '_blank');
    cy.get('a[href="https://andysmanclub.co.uk/"]').should('have.attr', 'target', '_blank');
  });

  it('should have scripts loaded for animations and sliders', () => {
    cy.get('script[src*="Animated-Type-Heading"]').should('exist');
    cy.get('script[src*="swiper-bundle"]').should('exist');
    cy.get('script[src*="responsive-blog-card-slider"]').should('exist');
  });

});
