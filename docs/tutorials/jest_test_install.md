-

## Tutorial: Setting Up Jest, Puppeteer, Cypress, jsdom, and Live Server

### 1. **Prerequisites**

Ensure you have Node.js and npm installed. If not, download and install them from [nodejs.org](https://nodejs.org/).

### 2. **Initialize Your Project**

If you haven’t already initialized your project with npm, navigate to your project directory in your terminal and run:

```bash
npm init -y
```

This will create a `package.json` file if one does not already exist.

### 3. **Install Testing and Development Tools**

To install Jest, Puppeteer, and other testing tools, run:

```bash
npm install --save-dev jest jest-html-reporter jest-junit jest-puppeteer jsdom puppeteer
```

This command installs:
- `jest`: JavaScript testing framework.
- `jest-html-reporter`: Generates HTML test reports.
- `jest-junit`: Outputs test results in JUnit format.
- `jest-puppeteer`: Provides integration with Puppeteer for end-to-end testing.
- `jsdom`: Simulates a browser environment for testing.
- `puppeteer`: Headless browser for testing.

To install Cypress, run:

```bash
npm install --save-dev cypress
```

To install `live-server` for serving your project locally, run:

```bash
npm install --save-dev live-server
```

### 4. **Configure Jest**

Ensure your `package.json` contains the following Jest configuration:

```json
"jest": {
  "testResultsProcessor": "jest-junit",
  "reporters": [
    "default",
    [
      "jest-html-reporter",
      {
        "publicPath": "./html-report",
        "filename": "report.html",
        "openReport": true
      }
    ]
  ],
  "clearMocks": true,
  "cacheDirectory": "jest_cache",
  "testEnvironment": "jsdom",
  "moduleFileExtensions": [
    "js",
    "json"
  ],
  "moduleNameMapper": {
    "\\.(css|less|sass|scss)$": "identity-obj-proxy"
  },
  "roots": [
    "<rootDir>"
  ],
  "testMatch": [
    "**/__tests__/**/*.test.js"
  ],
  "testRunner": "jest-circus/runner",
  "preset": "jest-puppeteer",
  "testTimeout": 30000
}
```

### 5. **Configure Live Server**

Add a script in your `package.json` to run `live-server` on port `5500`:

```json
"scripts": {
  "test": "jest",
  "test:cy": "cypress open", // For running Cypress tests
  "start:server": "live-server --port=5500"
}
```

### 6. **Run Your Tests**

**Jest Tests:**

To run Jest tests, use:

```bash
npm test
```

**Puppeteer Tests:**

Jest-Puppeteer integration will use the `jest` command to run Puppeteer tests. Ensure you have your Puppeteer tests written in files within your `__tests__` directory or as specified by your `testMatch` configuration.

**Cypress Tests:**

To open the Cypress test runner, use:

```bash
npm run test:cy
```

Cypress will open a graphical interface where you can run and interact with your tests.

### 7. **Start the Live Server**

To start the live server on port `5500`, use:

```bash
npm run start:server
```

Navigate to `http://localhost:5500` in your web browser to view your project.

### 8. **Verify Your Configuration**

- **Jest Tests**: Ensure Jest runs and passes your tests by checking the output in the terminal.
- **Puppeteer Tests**: Ensure Puppeteer tests run smoothly as part of the Jest test suite.
- **Cypress Tests**: Interact with the Cypress test runner and ensure your end-to-end tests are working as expected.
- **Live Server**: Confirm the live server is serving your project correctly by visiting `http://localhost:5500`.

### 9. **Additional Resources**

- [Jest Documentation](https://jestjs.io/docs/en/getting-started)
- [Puppeteer Documentation](https://pptr.dev/)
- [Cypress Documentation](https://docs.cypress.io/)
- [Live Server Documentation](https://www.npmjs.com/package/live-server)
- [jsdom Documentation](https://github.com/jsdom/jsdom)

### Summary

This tutorial has guided you through setting up Jest, Puppeteer, Cypress, jsdom, and Live Server for your project. You can now efficiently write, run, and manage unit, integration, and end-to-end tests while serving your project locally.

---
