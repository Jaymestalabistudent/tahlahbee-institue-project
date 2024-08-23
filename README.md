### Tahlahbee Institute Blog - Debug Branch

#### Overview
This repository contains the debug branch of the Tahlahbee Institute blog’s core Python application. This branch is specifically intended for testing and debugging purposes. Use this branch to identify and fix issues before deploying changes to the Deployment or Development branches. The Core Branch remains the foundational framework providing essential functionality and basic routes for the blog site.

#### Purpose
The main goal of this branch is to facilitate testing and debugging of the core blog features. It includes the fundamental components required for a Python web application, such as route handling, form processing, and basic template rendering, with additional focus on troubleshooting and test integration.

#### Current State
The Debug Branch is actively used for testing and includes various tests to validate functionality. While it establishes the basic structure, it may not have the advanced features required for a fully functional blog. It is intended for local testing and debugging.

#### Features
- **Basic Routes**: Includes minimal route definitions for core functionalities like template rendering and form processing.
- **Template Structure**: Utilizes Jinja2 templates for HTML page rendering.
- **Form Handling**: Contains simple form processing logic, extendable for user input and blog submissions.
- **Testing**: Includes tests to verify the functionality of routes, forms, and other core components.

#### Usage
To run the application and execute tests, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/tahlahbee-institue-project.git
   ```

2. **Set Up the Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: source venv/Scripts/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python run.py
   ```

5. **Run Tests**:
   Tests can be executed to ensure functionality:
   ```bash
   pytest
   ```

#### Future Development
This branch is designed for identifying issues and testing new features. Future enhancements can build upon this framework, including adding more dynamic features, integrating a database, and implementing user authentication.

#### Conclusion
The Debug Branch provides a platform for testing and debugging the Tahlahbee Institute blog. It includes the core functionality and test infrastructure needed to ensure reliability before merging changes into the Deployment or Development branches. This branch serves as a critical step in refining and enhancing the blog application.
