# To install `http-server` and run tests on your local machine, follow these steps:

1. **Install `http-server` globally**:

   ```bash
   npm install -g http-server
   ```
2. **Run `http-server`**:

   ```bash
   http-server
   ```
3. **Access the local server**:
   Open your web browser and navigate to the following URL:

   ```
   http://localhost:8080
   ```

   This will display the contents served by `http-server` on your local machine.
4. **Using log files and HAR files**:
   After running your tests, you can find the log files and HAR files in the `offline-tests-results/modal-tests` folder. These files contain detailed information about the interactions between your web browser and the served content.
5. **Viewing HAR files**:
   To view the HAR files, you can use tools like [Google&#39;s HAR Analyzer](https://toolbox.googleapps.com/apps/har_analyzer/). Simply upload the HAR file to the analyzer, and it will provide a detailed analysis of the interactions captured in the file.

By following these steps, you can effectively test your content using `http-server` on your local machine and analyze the results using log files and HAR files.
