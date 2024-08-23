# Tahlabbee Institute FlaskBlog

Welcome to the Tahlabbee Institute FlaskBlog repository! This project is a basic blog application built using Flask. It includes user authentication, a blog system, and is structured to support multiple development environments. 

## Repository Structure

The repository is organized into separate components:

1. **Backend**: This is where the core functionality of the blog resides. It includes user authentication, blog management, and other server-side logic.
2. **Frontend**: This contains the static and dynamic assets for the user interface.

## Branches

### Core Branch

- **Purpose**: This branch serves as the original testing ground during the initial development phase.
- **Usage**: It is primarily used to test core functionalities and make initial adjustments.

### Development Branch

- **Purpose**: This branch is for ongoing development and testing. It includes features and changes that are being worked on before they are ready for production.
- **Usage**: Developers should push new features and updates here and test them thoroughly.

### Production Branch

- **Purpose**: This branch contains the code that is ready for deployment. It should be stable and free of issues.
- **Usage**: Use this branch for the live version of the blog. All tested and approved features from the Development branch should be merged here.

## Features

- **User Authentication**: Secure login and registration system.
- **Blog Management**: Create, read, update, and delete blog posts.
- **User Pages**: Personalized pages for users to manage their profiles and content.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)
- Virtualenv (recommended for managing dependencies)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/tahlabbee-blog.git
   cd tahlabbee-blog
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**

   ```bash
   flask db upgrade
   ```

5. **Run the Application**

   ```bash
   flask run
   ```

   The application should now be running at `http://127.0.0.1:5000/`.

### Testing

1. **Run Tests**

   ```bash
   pytest
   ```

   Ensure all tests pass before merging changes into the `production` branch.

## Contributing

1. **Create a New Branch**

   ```bash
   git checkout -b feature-branch
   ```

2. **Make Your Changes**

3. **Commit Your Changes**

   ```bash
   git add .
   git commit -m "Description of changes"
   ```

4. **Push to the Development Branch**

   ```bash
   git push origin feature-branch
   ```

5. **Create a Pull Request**

   Open a pull request from your `feature-branch` to the `development` branch for review.

## Deployment

To deploy the application, merge the `development` branch into the `production` branch and follow your deployment process (e.g., using Docker, Heroku, or any cloud service).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please reach out to [your-email@example.com](mailto:your-email@example.com).

Thank you for contributing to the Tahlabbee Institute FlaskBlog!