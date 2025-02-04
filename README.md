# Gsecart Backend and Streamlit Application

This project consists of a FastAPI backend, a Streamlit frontend, and an SQLite3 database, all containerized using Docker. The backend uses **SQLAlchemy** for database interactions, enabling seamless communication with the SQLite3 database.

## Technologies Used
- **FastAPI**: Backend framework to handle REST API requests.
- **Streamlit**: Frontend framework for interactive dashboards and user interfaces.
- **SQLite3**: Lightweight relational database for storing data.
- **SQLAlchemy**: ORM for database interaction in the backend.
- **Docker**: Containerization of the application for easy deployment and management.

## Project Setup

### Requirements
- Docker
- Docker Compose

### Steps to Run the Application

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2. **Build and start the containers** using Docker Compose:
    ```bash
    docker-compose up --build
    ```

3. **Access the services**:
    - **Streamlit App**: 
      Open your browser and visit [http://182.64.21.255:8501](http://182.64.21.255:8501) to access the Streamlit app.
    - **FastAPI Backend**: 
      The backend will be available at `http://localhost:8000` (for local development) or `http://<your-ip>:8000` if running remotely.

4. **Database**:
    - **SQLite3** is used for local, lightweight database storage. The SQLite3 database file is included in the project and is configured in the backend using SQLAlchemy. No additional configuration is required for the database to work.

    - The database file `grecart_db.db` is used by the backend, and it will be created automatically when the application is started if it doesn't exist.

    - **SQLAlchemy** manages the database tables and relationships via ORM, so ensure that the models are properly set up for your application needs.

### Project Structure

- **Dockerfile**: Defines the backend container image for FastAPI.
- **docker-compose.yml**: Configures the services, including backend, Streamlit frontend, and SQLite3 database.
- **.dockerignore**: Specifies which files and directories to exclude when building the Docker image.
- **models.py**: SQLAlchemy models for database tables.
- **main.py**: FastAPI app configuration and startup.
- **schemas.py**: Defines the Pydantic models (schemas) for request and response validation.
- **database.py**: Handles database connection and session management with SQLAlchemy.
- **crud.py**: Contains the functions for interacting with the database, including create, read, update, and delete operations.
- **endpoint.py**: Defines the FastAPI routes/endpoints and integrates the CRUD functions.

### Notes
- This setup uses SQLite3 for local development, so no need for additional database services like PostgreSQL.
- To stop the services, run `docker-compose down` to bring down the containers.
- SQLAlchemy manages the database tables and relationships via ORM, so ensure that the models are properly set up for your application needs.


