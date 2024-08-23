
---

## Test Error Report and Fixes

### Errors

1. **Sign-in Button Redirection**
   ```plaintext
   expect(signInButton.onclick).toBeInstanceOf(Function);
   ```
   **Issue**: Tests expect the `onclick` handler to be a `Function`, but it’s not behaving as expected.

2. **Recipes Button Redirection**
   ```plaintext
   expect(recipesButton.onclick.toString()).toContain("window.location.href='subpages/recipe.html'");
   ```
   **Issue**: Actual handler redirects to `https://tahlahbee-institute-project.onrender.com/register` instead of `subpages/recipe.html`.

3. **Our Stories Button Redirection**
   ```plaintext
   expect(storiesButton.onclick.toString()).toContain("window.location.href='subpages/story.html'");
   ```
   **Issue**: Same as above, handler redirects to an unexpected URL.

4. **Get Help Button Redirection**
   ```plaintext
   expect(helpButton.onclick.toString()).toContain("window.location.href='subpages/mental.html'");
   ```
   **Issue**: Handler redirects incorrectly.

5. **Spotify Button Redirection**
   ```plaintext
   expect(spotifyButton.onclick.toString()).toContain("window.location.href='subpages/spotify.html'");
   ```
   **Issue**: Handler has an incorrect URL.

6. **Contact Us Button Redirection**
   ```plaintext
   expect(contactButton.onclick.toString()).toContain("window.location.href='subpages/contact.html'");
   ```
   **Issue**: Same issue with URL mismatch.

### Causes

- **Incorrect Redirection URLs**: Handlers redirect to `https://tahlahbee-institute-project.onrender.com/register` instead of expected URLs.
- **Improper Test Assertions**: Tests check the `onclick` function’s string representation rather than the actual redirection.

### Fixes

1. **Update Button Handlers**:
   Ensure `onclick` handlers point to the correct URLs:

   ```javascript
   document.querySelector('button#signIn').onclick = function() {
       window.location.href = 'subpages/signin.html';
   };
   ```

2. **Revise Test Cases**:
   Simulate button clicks and check redirection results:

   ```javascript
   beforeEach(() => {
       delete window.location;
       window.location = { href: '' };
   });

   test('Sign-in button redirects correctly', () => {
       const signInButton = document.querySelector('button#signIn');
       expect(signInButton).not.toBeNull();
       signInButton.click(); // Simulate click
       expect(window.location.href).toBe('subpages/signin.html');
   });

   // Apply similar updates for other buttons
   ```

3. **Verify Test Environment**:
   Ensure the test environment correctly simulates interactions and validates outcomes.



Certainly! Here’s a concise report on the errors and their fixes:

---

## Test Error Report and Fixes

### Errors

1. **Error: Invalid Selector for `<h2>` Titles**
   ```plaintext
   SyntaxError: 'h2:contains('Early 2022')' is not a valid selector

     43 |         expectedTitles.forEach(title => {
     45 |             const h2Element = document.querySelector(`h2:contains('${title}')`);
     |                                        ^
   ```
   **Issue**: `:contains` is not a valid CSS selector in `querySelector`.

2. **Error: Metadata Content Mismatch**
   ```plaintext
   expect(received).toBe(expected) // Object.is equality

   - Expected  - 0
   + Received  + 1

     72 |     test('metadata is correct', () => {
     74 |         expect(metaDescription.content).toBe('Tahlahbee Institute is a dedicated self-help website for single fathers, offering a wide range of eBooks, advice courses, and inspirational quotes to support and empower single dads on their journey');
     |                                         ^
   ```
   **Issue**: The actual metadata content does not match the expected value.

3. **Error: Footer Element Missing**
   ```plaintext
   expect(received).not.toBeNull()

   Received: null

     81 |     test('footer exists', () => {
     82 |         const footer = document.querySelector('footer');
     > 83 |         expect(footer).not.toBeNull();
     |                            ^
   ```
   **Issue**: The `<footer>` element was not found in the DOM.

### Fixes

1. **Fix for `<h2>` Titles Selector**
   - **Issue**: `:contains` is not supported in CSS selectors.
   - **Fix**: Use JavaScript to find and verify titles.

   ```javascript
   test('all <h2> titles are correct', () => {
       const expectedTitles = ['Early 2022', 'Mid 2022', 'Late 2022'];
       const h2Elements = document.querySelectorAll('h2');
       
       expectedTitles.forEach(title => {
           const found = Array.from(h2Elements).some(h2 => h2.textContent === title);
           expect(found).toBe(true);
       });
   });
   ```

2. **Fix for Metadata Content**
   - **Issue**: The actual metadata content does not match the expected value.
   - **Fix**: Ensure the HTML metadata matches the expected content.

   ```javascript
   test('metadata is correct', () => {
       const metaDescription = document.querySelector('meta[name="description"]');
       expect(metaDescription.content).toBe('Tahlahbee Institute is a dedicated self-help website for single fathers, offering a wide range of eBooks, advice courses, and inspirational quotes to support and empower single dads on their journey');
       
       const metaKeywords = document.querySelector('meta[name="keywords"]');
       expect(metaKeywords.content).toBe('single fathers, self-help, eBooks, advice courses, inspirational quotes, single dads, parenting, fatherhood, support for fathers, empowerment for dads');
   });
   ```

3. **Fix for Footer Element Existence**
   - **Issue**: `<footer>` element is missing.
   - **Fix**: Verify that the `<footer>` element exists in the DOM.

   ```javascript
   test('footer exists', () => {
       const footer = document.querySelector('footer');
       expect(footer).not.toBeNull();
   });
   ```




Certainly! Here’s a concise report on the `Bookshop Page` test error and its fix:

---

## Test Error Report and Fixes

### Error

**Error: Meta Tags Content Mismatch**
```plaintext
expect(received).toBe(expected) // Object.is equality

- Expected  - 0
+ Received  + 1

  Tahlahbee Institute is a dedicated self-help website for single fathers, offering a wide range of eBooks, advice courses, and inspirational quotes to support and empower single dads on their journey
+
  54 |     const metaKeywords = document.querySelector('meta[name="keywords"]');
  55 |
  > 56 |     expect(metaDescription.getAttribute('content')).toBe('Tahlahbee Institute is a dedicated self-help website for single fathers, offering a wide range of eBooks, advice courses, and inspirational quotes to support and empower single dads on their journey');
     |                                                     ^
  57 |     expect(metaKeywords.getAttribute('content')).toBe('single fathers, self-help, eBooks, advice courses, inspirational quotes, single dads, parenting, fatherhood, support for fathers, empowerment for dads');
  58 |   });
  59 | });

  at Object.toBe (__test__/books.test.js:56:53)
```

**Issue**: The actual meta tag content does not match the expected value.

### Fix

1. **Verify Meta Tag Content**:
   Ensure the meta tag's `content` attribute matches the expected values. If the content is not as expected, adjust either the HTML or the test expectations accordingly.

   **Updated Test Code**:
   ```javascript
   test('meta tags are correctly set', () => {
       const metaDescription = document.querySelector('meta[name="description"]');
       const metaKeywords = document.querySelector('meta[name="keywords"]');
       
       // Verify the content of the meta description
       expect(metaDescription.getAttribute('content')).toBe('Tahlahbee Institute is a dedicated self-help website for single fathers, offering a wide range of eBooks, advice courses, and inspirational quotes to support and empower single dads on their journey');
       
       // Verify the content of the meta keywords
       expect(metaKeywords.getAttribute('content')).toBe('single fathers, self-help, eBooks, advice courses, inspirational quotes, single dads, parenting, fatherhood, support for fathers, empowerment for dads');
   });
   ```

2. **Ensure Meta Tags are Correct**:
   Confirm that the meta tags in your HTML match the expected values used in the tests. Update the HTML if needed to align with the test expectations.

### Summary

- **Update Test Expectations**: Ensure that the expected values in your test cases match the actual values set in your HTML meta tags.
- **Verify Meta Tags**: Check the meta tags in your HTML to ensure they are correctly set.

- **Update Selector**: Replace invalid CSS selectors with JavaScript logic for title verification.
- **Check Metadata**: Ensure metadata content matches expected values.
- **Verify Elements**: Confirm that key elements like the footer exist in the DOM.

Update button handlers to the correct URLs and revise tests to simulate clicks and check results directly to resolve these issues.
