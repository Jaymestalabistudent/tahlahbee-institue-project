
# Step-by-Step Guide to Using Jest for Testing HTML Pages

#### 1. Initialize Your Project

First, initialize a new Node.js project:

```sh
npm init -y
```

#### 2. Install Required Packages

Install Jest, jsdom, and the reporters:

```sh
npm install --save-dev jest jsdom jest-html-reporter jest-junit-reporter
```

#### 3. Create Test Directory and Files

Create a directory for your tests and an initial test file:

```sh
mkdir __tests__
touch __tests__/index.test.js
```

#### 4. Add Test Code (Optional)

Add your test code to `__tests__/index.test.js`. Here's an example of a simple test:

```javascript
// __tests__/index.test.js
const { JSDOM } = require('jsdom');

test('checks if the title is correct', () => {
  const dom = new JSDOM(`<!DOCTYPE html><html><head><title>Test Page</title></head><body></body></html>`);
  const title = dom.window.document.querySelector('title').textContent;
  expect(title).toBe('Test Page');
});
```

#### 5. Configure Jest in `package.json`

Add the following configuration to your `package.json` file:

```json
{
  "scripts": {
    "test": "jest"
  },
  "dependencies": {
    "jsdom": "^24.0.0"
  },
  "devDependencies": {
    "jest": "^29.7.0",
    "jest-html-reporter": "^3.10.2",
    "jest-junit-reporter": "^1.1.0"
  },
  "jest": {
    "testResultsProcessor": "./node_modules/jest-junit-reporter",
    "reporters": [
      "default",
      ["jest-html-reporter", {
        "publicPath": "./html-report",
        "filename": "report.html",
        "openReport": true
      }]
    ]
  }
}
```

#### 6. Run Your Tests

Run your tests using the following command:

```sh
npm test
```

#### 7. View the HTML Report

After running the tests, an HTML report will be generated in the `html-report` directory. Open the `report.html` file to view the test results.

#### 8. Move Test Results to Offline Folder (Optional)

If you want to move the test results to an offline folder, you can create a script to do so. For example, you can add a post-test script in your `package.json`:

```json
{
  "scripts": {
    "test": "jest",
    "posttest": "mv html-report offline-tests-results"
  }
}
```

Now, when you run `npm test`, the HTML report will be moved to the `offline-tests-results` folder.

### Conclusion

By following these steps, you can set up Jest to test HTML pages and generate HTML reports. For more information, you can visit the [npm documentation](https://www.npmjs.com/).
