/// <reference types="cypress" />

describe('Bookshop Page', () => {
  beforeEach(() => {
    // Visit the bookshop page before each test
    cy.visit('books.html');
  });

  it('should display the page title correctly', () => {
    cy.title().should('include', 'Bookshop');
  });

  it('should display the heading with the correct text', () => {
    cy.get('h1').should('have.text', 'Bookstore');
  });

  it('should display a subtitle with the correct text', () => {
    cy.get('p.text-center').should('have.text', 'Download Books and Increase Your Knowledge');
  });

  it('should display a list of book cards', () => {
    cy.get('.card').should('have.length', 6); // Ensure there are 6 book cards
  });

  it('should display the correct title for each book', () => {
    const titles = [
      'Food : A Guide',
      'Meditation : A Journey',
      'Fitness 4 U',
      'Stress Free',
      '5 Steps',
      'Developing Courage'
    ];

    cy.get('.card').each((card, index) => {
      cy.wrap(card).find('.card-title').should('contain.text', titles[index]);
    });
  });

  it('should have download buttons for each book', () => {
    cy.get('.btn.btn-dark').should('have.length', 6); // Ensure there are 6 download buttons
  });

  it('should have correct download links for each book', () => {
    const links = [
      'https://drive.google.com/uc?export=download&id=1-0_KzROmxL4rtFn35z0WSnsY1d3bin57',
      'https://drive.google.com/uc?export=download&id=1-3CRVcE0_CoDImc0lRNAtuxYkdctfZwV',
      'https://drive.google.com/uc?export=download&id=1-poM9P3ZP1mnRxt5r9ZIWIkeGmLdSyS1',
      'https://drive.google.com/uc?export=download&id=1-kZNh-xklK1aJ5mVq6lkcUlLZCIhVVNZ',
      'https://drive.google.com/uc?export=download&id=1-_s0cN9V8qZ4mc2HoL245h_YlmnSmORJ',
      'https://drive.google.com/uc?export=download&id=1-G-RcHD6pYzHLl94O-_M75KzAKk6xfFn'
    ];

    cy.get('.btn.btn-dark').each((button, index) => {
      cy.wrap(button).should('have.attr', 'href', links[index]);
    });
  });

  it('should have correct alt text for each book image', () => {
    const altTexts = [
      'food book',
      'meditation',
      'fitness book',
      'stress control',
      '5 steps',
      'courage book'
    ];

    cy.get('.card-img-top').each((img, index) => {
      cy.wrap(img).should('have.attr', 'alt', altTexts[index]);
    });
  });
});
