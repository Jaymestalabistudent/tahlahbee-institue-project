const { defineConfig } = require("cypress");
const MochawesomeReporter = require('cypress-mochawesome-reporter/plugin');

module.exports = defineConfig({
  projectId: "s485k9",
  e2e: {
    setupNodeEvents(on, config) {
      MochawesomeReporter(on); // Register the Mochawesome reporter plugin
      // Other event listeners
    },
    specPattern: "cypress/e2e/**/*.spec.js",
  },
  reporter: "mochawesome",
  reporterOptions: {
    reportDir: "cypress/reports",
    overwrite: true,
    html: true,
    json: true,
  },
  screenshotsFolder: "cypress/screenshots",
  video: false,
});
