

# Flask Blog Setup

## **Bash Terminal Commands**

1. **Create a project directory and navigate into it:**
    ```bash
    mkdir flask_blog
    cd flask_blog
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install Flask:**
    ```bash
    pip install Flask
    ```

5. **Install Flask-SQLAlchemy for ORM:**
    ```bash
    pip install Flask-SQLAlchemy
    ```

6. **Install Flask-Migrate for handling database migrations:**
    ```bash
    pip install Flask-Migrate
    ```

7. **Install PostgreSQL adapter for Python:**
    ```bash
    pip install psycopg2-binary
    ```

8. **Create a `requirements.txt` file with current packages:**
    ```bash
    pip freeze > requirements.txt
    ```

9. **Initialize a Git repository:**
    ```bash
    git init
    ```

10. **Create a basic Flask app file:**
    ```bash
    touch app.py
    ```

11. **Create a `.gitignore` file:**
    ```bash
    touch .gitignore
    ```

12. **Add common files and directories to `.gitignore`:**
    ```bash
    echo "venv/" >> .gitignore
    echo "__pycache__/" >> .gitignore
    echo ".env" >> .gitignore
    echo "instance/" >> .gitignore
    ```

13. **Create a `config.py` file for configuration:**
    ```bash
    touch config.py
    ```

14. **Create a `models.py` file for database models:**
    ```bash
    touch models.py
    ```

15. **Create a `migrations` directory:**
    ```bash
    mkdir migrations
    ```

16. **Initialize Flask-Migrate:**
    ```bash
    flask db init
    ```

17. **Generate the initial migration scripts:**
    ```bash
    flask db migrate -m "Initial migration."
    ```

18. **Apply the migrations to the database:**
    ```bash
    flask db upgrade
    ```

19. **Run the Flask development server:**
    ```bash
    flask run
    ```

20. **Check installed packages in the virtual environment:**
    ```bash
    pip list
    ```

---

# PostgreSQL Commands

1. **Log in to PostgreSQL:**
    ```bash
    psql -U postgres
    ```

2. **Create a new database:**
    ```sql
    CREATE DATABASE flask_blog;
    ```

3. **Connect to the new database:**
    ```sql
    \c flask_blog
    ```

4. **Create a new user with a password:**
    ```sql
    CREATE USER flask_user WITH PASSWORD 'password';
    ```

5. **Grant privileges to the user on the database:**
    ```sql
    GRANT ALL PRIVILEGES ON DATABASE flask_blog TO flask_user;
    ```

6. **List all databases:**
    ```sql
    \l
    ```

7. **List all tables in the current database:**
    ```sql
    \dt
    ```

8. **Show details about a specific table:**
    ```sql
    \d tablename
    ```

9. **Drop a database:**
    ```sql
    DROP DATABASE flask_blog;
    ```

10. **Drop a user:**
    ```sql
    DROP USER flask_user;
    ```

11. **Create a table:**
    ```sql
    CREATE TABLE posts (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100),
        content TEXT
    );
    ```

12. **Insert data into a table:**
    ```sql
    INSERT INTO posts (title, content) VALUES ('First Post', 'This is the content of the first post.');
    ```

13. **Select data from a table:**
    ```sql
    SELECT * FROM posts;
    ```

14. **Update data in a table:**
    ```sql
    UPDATE posts SET content = 'Updated content' WHERE id = 1;
    ```

15. **Delete data from a table:**
    ```sql
    DELETE FROM posts WHERE id = 1;
    ```

16. **List all users:**
    ```sql
    \du
    ```

17. **Show user privileges:**
    ```sql
    \dp
    ```

18. **View current database settings:**
    ```sql
    SHOW ALL;
    ```

19. **Change user password:**
    ```sql
    ALTER USER flask_user WITH PASSWORD 'newpassword';
    ```

20. **Quit PostgreSQL:**
    ```sql
    \q
    ```

---

# GitHub Commands

1. **Check the status of your Git repository:**
    ```bash
    git status
    ```

2. **Add all changes to the staging area:**
    ```bash
    git add .
    ```

3. **Commit changes with a message:**
    ```bash
    git commit -m "Initial commit"
    ```

4. **View the commit history:**
    ```bash
    git log
    ```

5. **Create a new branch:**
    ```bash
    git branch new-branch
    ```

6. **Switch to a new branch:**
    ```bash
    git checkout new-branch
    ```

7. **Merge a branch into the current branch:**
    ```bash
    git merge new-branch
    ```

8. **Delete a branch:**
    ```bash
    git branch -d new-branch
    ```

9. **Push changes to GitHub:**
    ```bash
    git push origin main
    ```

10. **Pull the latest changes from GitHub:**
    ```bash
    git pull origin main
    ```

11. **Clone a repository:**
    ```bash
    git clone https://github.com/username/repository.git
    ```

12. **Add a remote repository:**
    ```bash
    git remote add origin https://github.com/username/repository.git
    ```

13. **Remove a remote repository:**
    ```bash
    git remote remove origin
    ```

14. **View remote repositories:**
    ```bash
    git remote -v
    ```

15. **Tag a commit:**
    ```bash
    git tag -a v1.0 -m "Version 1.0"
    ```

16. **Push tags to GitHub:**
    ```bash
    git push origin --tags
    ```

17. **Rebase a branch:**
    ```bash
    git rebase main
    ```

18. **View differences between commits:**
    ```bash
    git diff commit1 commit2
    ```

19. **Discard local changes:**
    ```bash
    git checkout -- file.txt
    ```

20. **Amend the last commit:**
    ```bash
    git commit --amend
    ```
