
### Step 1: Install Node.js and npm
Cypress requires Node.js and npm (Node Package Manager). If you don't have them installed, follow these steps:

1. Download and install Node.js from the [official website](https://nodejs.org/).
2. Verify the installation:
   ```sh
   node -v
   npm -v
   ```

### Step 2: Initialize a New Project
1. Create a new directory for your project and navigate into it:
   ```sh
   mkdir my-cypress-project
   cd my-cypress-project
   ```
2. Initialize a new npm project:
   ```sh
   npm init -y
   ```

### Step 3: Install Cypress
1. Install Cypress as a development dependency:
   ```sh
   npm install cypress --save-dev
   ```

2. Open Cypress for the first time to complete the installation:
   ```sh
   npx cypress open
   ```

This will create a `cypress` directory with sample tests.

### Step 4: Write Your First Test
1. Create a new test file in `cypress/integration`. For example, `example_spec.js`:
   ```js
   // cypress/integration/example_spec.js
   describe('My First Test', () => {
     it('Visits the Kitchen Sink', () => {
       cy.visit('https://example.cypress.io')
       cy.contains('type').click()
       cy.url().should('include', '/commands/actions')
       cy.get('.action-email').type('fake@email.com').should('have.value', 'fake@email.com')
     })
   })
   ```

### Step 5: Install Mochawesome Reporter
1. Install Mochawesome and related plugins:
   ```sh
   npm install mochawesome mochawesome-merge mochawesome-report-generator --save-dev
   ```

2. Configure Cypress to use Mochawesome:
   - Add the following to your `cypress.json` file:
     ```json
     {
       "reporter": "mochawesome",
       "reporterOptions": {
         "reportDir": "cypress/reports",
         "overwrite": false,
         "html": false,
         "json": true
       },
       "screenshotsFolder": "cypress/screenshots",
       "video": false
     }
     ```

### Step 6: Capture Screenshots of Failed Tests
1. Cypress automatically captures screenshots of failed tests if the `screenshotsFolder` is specified in `cypress.json`.

### Step 7: Run Tests and Generate Report
1. Run your Cypress tests:
   ```sh
   npx cypress run
   ```

2. Merge the generated JSON reports:
   ```sh
   npx mochawesome-merge cypress/reports/*.json > cypress/reports/report.json
   ```

3. Generate the HTML report:
   ```sh
   npx marge cypress/reports/report.json -f report -o cypress/reports
   ```

### Step 8: View the Report and Screenshots
1. Open the generated HTML report located in `cypress/reports/report.html` with your web browser.
2. Check the `cypress/screenshots` folder for screenshots of failed tests.

### Step 9: Automate the Process (Optional)
To automate the process of running tests and generating reports, you can add scripts to your `package.json`:
```json
"scripts": {
  "cypress:run": "cypress run",
  "report:merge": "mochawesome-merge cypress/reports/*.json > cypress/reports/report.json",
  "report:generate": "marge cypress/reports/report.json -f report -o cypress/reports",
  "test:report": "npm run cypress:run && npm run report:merge && npm run report:generate"
}
```

Now you can run your tests and generate the report with a single command:
```sh
npm run test:report
```