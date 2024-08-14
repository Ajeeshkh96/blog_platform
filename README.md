# Project Name

 **blog_platform** : It is an assignment given by the company contact point 360.
 
## Overview

This project is a Django application that includes user signup, login, and blog CRUD functionalities. The project is containerized using Docker for easy deployment and management.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup and Run

1. **Clone the Repository**

    ```bash
    git clone <your-repository-url>
    cd <your-project-directory>
    ```

2. **Create a `.env` File**

    Create a `.env` file in the project root directory with the following content:

    ```env
    POSTGRES_DB=mydatabase
    POSTGRES_USER=myuser
    POSTGRES_PASSWORD=mypassword
    DJANGO_DB_NAME=mydatabase
    DJANGO_DB_USER=myuser
    DJANGO_DB_PASSWORD=mypassword
    DJANGO_DB_HOST=db
    ```

3. **Build and Start Containers**

    ```bash
    docker-compose up --build
    ```

4. **Apply Migrations**

    If necessary, apply database migrations:

    ```bash
    docker-compose run web python manage.py migrate
    ```

5. **Create a Superuser**

    To create a superuser for accessing Django Admin:

    ```bash
    docker-compose run web python manage.py createsuperuser
    ```

6. **Access the Application**

    - The application will be available at `http://localhost:8000`.

### Endpoints

You can test the following endpoints using Postman or any HTTP client:

- **Signup**: `POST http://localhost:8000/signup/`
  - Body: JSON object with user details (e.g., `username`, `password`, `email`, `address`, `pincode`, `dob`)

- **Login**: `POST http://localhost:8000/login/`
  - Body: JSON object with `username` and `password`
  - Returns: JWT tokens (access and refresh tokens)

- **List Blogs**: `GET http://localhost:8000/blog/blogs/`
  - Returns: List of all blog entries

- **Update Blog**: `PUT/PATCH http://localhost:8000/blog/blogs/<id>/`
  - URL Parameters: `id` of the blog entry to update
  - Body: JSON object with updated blog details (e.g., `blog_name`, `blog_content`, `publish_date`, `image`)

- **Delete Blog**: `DELETE http://localhost:8000/blog/blogs/<id>/`
  - URL Parameters: `id` of the blog entry to delete
  - Returns: Status message indicating successful deletion

## Troubleshooting

- **Database Migration Issues**: If you encounter errors related to database schema, ensure migrations are applied correctly by running `docker-compose run web python manage.py migrate`.

- **Container Not Starting**: Check Docker logs for errors with `docker-compose logs` and ensure all services are configured correctly.

## Contributing

Feel free to submit issues or pull requests to improve the project.
