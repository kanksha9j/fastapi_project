# fastapi_project 
This project is created to locate nearby charging stations and enter the data into a PostgreSQL database initially and later into PostGIS. The project is aimed at learning the basics of Python and related tech stack, including FastAPI, PostgreSQL, Docker and pytest.

Steps to Setup

1. Created Python virtual environment with Python 3.10 in VSCode
- pip install virtualenv (if not already installed)
- python -m venv .venv

2. Activate environment:

- Windows: .venv\Scripts\activate.bat
- Linux/Mac: source .venv/bin/activate
- Verify with python --version

3. Installed FastAPI and created main.py
- pip install "fastapi[standard]"
- Run in dev mode: fastapi dev main.py (or uvicorn main:app --reload)

4. Setup GitHub project

- git init
- Create .gitignore and add .venv and __pycache__
- git add .
- git commit -m "Initial commit"
- git remote add origin https://github.com/kanksha9j/fastapi_project.git
- git push -u origin main

5. Setup PostgreSQL in Docker
- Install Docker Desktop (and WSL on Windows if needed: wsl --install)
- Create docker-compose.yml with PostgreSQL image, ports, environment variables
- Start database: docker compose up
- Connected PostgreSQL database inside VSCode using PostgreSQL extension

6. Created routes and test files
- Installed pytest: pip install pytest
- Added test files in tests/ folder

7. Installed PostgreSQL database driver
- pip install psycopg2-binary
- Created db.py for database connection

8. Install pydantic settings, allows type-safe usage of environment variables.
- pip install pydantic-settings
- Create config.py, use Pydantic to define type-safe configuration. This file will be imported in db.py for database settings.
- Create chargingstation.py, use Pydantic to define a type-safe class for charging station attributes. Import and use this class in main.py to ensure type safety when handling charging station data.

9. Create requirements.txt, captures all installed packages for reproducibility.
- pip freeze > requirements.txt
- Create pytest.ini , Configure pytest, including environment variable support. Install support for environment variables in pytest: pip install pytest-env

10. Create PostgreSQL table using postgreSQL explorer in VSCode.

11. run pytest with: pytest -c app/tests/pytest.ini

12. Swagger and Docker setup:
- Swagger automatically generates a UI with documentation for your FastAPI application.
- In Dockerfile: Start with a base image. Copy your application files. Expose the FastAPI port.
- In docker-compose.yml: Add your backend service. Add a PostgreSQL service. Ensure both services can communicate. 
- Run your application; Swagger UI will be available for interactive API documentation.

