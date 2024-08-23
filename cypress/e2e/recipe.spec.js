// cypress/integration/recipe_page_tests.js

describe("Recipe Page Tests", () => {
  beforeEach(() => {
    cy.visit("subpages/recipe.html"); // Adjust the URL to your actual recipe page path
  });

  it("should display the navigation bar", () => {
    cy.get("nav.navbar").should("exist");
  });


  it("should display the preloader on page load", () => {
    cy.get("#pageloader").should("be.visible");
  });

  it("should hide the preloader after loading", () => {
    cy.get("#pageloader").should("be.visible");
    cy.wait(1000); // Wait for 1 second
    cy.get("#pageloader").should("not.be.visible");
  });

  it("should display the heading and description correctly", () => {
    cy.get("header.recipe-app-header").should("contain.text", "Recipe App");
    cy.get("header.recipe-app-header").should(
      "contain.text",
      "Simply type in the name of a dish and find out how to make it!"
    );
  });

  it("should display the search input and button", () => {
    cy.get("#recipe-app-user-inp").should("exist");
    cy.get("#recipe-app-search-btn").should("exist");
  });

  it("should accept text input", () => {
    cy.get("#recipe-app-user-inp").type("Pasta").should("have.value", "Pasta");
  });

  it("should have an empty result container initially", () => {
    cy.get("#recipe-app-result").should("be.empty");
  });

  it("should trigger a search button click event", () => {
    cy.get("#recipe-app-search-btn").click();
    // Assuming the search button should trigger an event,
    // you may need to verify the result in the result container
    cy.get("#recipe-app-result").should("be.visible");
  });

  it("should have the correct page title", () => {
    cy.title().should("include", "Recipes");
  });
});
