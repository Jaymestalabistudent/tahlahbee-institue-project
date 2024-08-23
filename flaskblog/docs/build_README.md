
## Getting Started with the Tahlahbee Institute Blog locally

The Tahlahbee Institute Blog is a Flask-based web application that allows users to create, read, update, and delete blog posts. It provides a simple and intuitive interface for managing blog content and interacting with readers. This guide will walk you through the process of setting up the Tahlahbee Institute Blog locally on your machine.

Please read the [branch_notes.md](branch_notes.md) for more information on the branches available for the project.

To get started with FlaskBlog, follow the steps below:

1. **Clone the Repository**: Open your terminal and run the following command to clone the FlaskBlog repository:

    ```
    git clone https://github.com/username/flask_blog.git
    ```

2. **Create a Virtual Environment**: Navigate to the project directory and create a virtual environment by running the following commands:

    ```
    cd flask_blog
    python -m venv venv
    ```

3. **Activate the Virtual Environment**: Activate the virtual environment by running the appropriate command based on your operating system:

    - For Windows:

      ```
      venv\Scripts\activate
      ```

    - For macOS/Linux:

      ```
      source venv/bin/activate
      ```

4. **Install Dependencies**: Once the virtual environment is activated, install the required dependencies by running the following command:

    ```
    pip install -r requirements.txt
    ```

5. **Run the Application**: Finally, start the FlaskBlog application by running the following command:

    ```
    python run.py
    ```

    The application will be accessible at `http://localhost:5000` in your web browser.

Congratulations! You have successfully set up and started the application. You can now explore the Tahlahbee Institute Blog locally and begin customizing it to suit your needs.

## Additional Resources

To further enhance your understanding of the Tahlahbee Institute Blog project, we recommend exploring the following resources:

- [Production Notes](production_notes.md): This document provides detailed information on deploying the project, including configuration settings, server requirements, and deployment strategies.

- [File Structure](file_structure.md): Learn more about the project's directory structure and organization. This document outlines the purpose of each directory and file, helping you navigate and understand the codebase more effectively.

- [Terminal Notes](terminal_notes.md): Gain insights into commonly used terminal commands that can streamline your development workflow. This resource covers essential commands for navigating directories, managing files, and executing scripts.

By referring to these resources, you'll have a comprehensive understanding of the Tahlahbee Institute Blog project and be well-equipped to contribute to its development. Happy coding!