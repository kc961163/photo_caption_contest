# Photo Caption Contest Backend

## Project Overview

The **Photo Caption Contest Backend** is a FastAPI-based server designed to power a platform where users can participate in photo caption contests. The server hosts a collection of images and provides endpoints for user authentication, caption submission, and administrative controls. Utilizing PostgreSQL for data storage and SQLAlchemy as the ORM, the backend ensures efficient data management and scalability. Comprehensive API documentation is available via Swagger, and the application is deployed on Render for accessibility.

## Technologies Used

- **Backend Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT (JSON Web Tokens)
- **Caching:** Redis (optional)
- **API Documentation:** Swagger UI (integrated with FastAPI)
- **Deployment:** Render
- **Version Control:** Git & GitHub
- **Environment Management:** Conda
- **Testing:** Postman
- **Migrations:** Alembic

## Features

### User Features
- **Registration:** Users can create an account.
- **Authentication:** Users can log in to receive a JWT for authenticated requests.
- **View Contest Images:** Users can view images available for captioning.
- **Create Captions:** Authenticated users can submit captions for contest images.
- **View Captions:** Users can view all captions for a specific image.
- **Like/Upvote Captions:** Users can like or upvote captions to highlight favorites.

### Administrator Features
- **Upload Images:** Administrators can add new images to the contest.
- **Manage Contests:** Administrators can start/end contests and select winners.
- **Manage Users:** Administrators can view, edit, or delete user accounts.
- **Moderate Captions:** Administrators can remove inappropriate captions.

### Additional Features
- **Caching:** Implement caching for frequently accessed data like contest images and captions to improve performance.
- **Comprehensive API Documentation:** Interactive Swagger UI documentation.
- **Robust Error Handling:** Ensure reliability and provide meaningful error messages.
- **Secure Deployment:** Host the application on Render for accessibility and scalability.

## Project Structure

```
photo_caption_contest/
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── api/
│   ├── __init__.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── controllers.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── captions/
│   │   ├── __init__.py
│   │   ├── controllers.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── images/
│   │   ├── __init__.py
│   │   ├── controllers.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── users/
│   │   ├── __init__.py
│   │   ├── controllers.py
│   │   ├── models.py
│   │   └── schemas.py
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       ├── crud.py
│       ├── dependencies.py
│       └── utils.py
├── main.py
├── .gitignore
├── README.md
├── requirements.txt
├── pyproject.toml
├── isort.cfg
└── environment.yml (optional)
```

- **`api/` Directory:** Contains all application logic.
  - **`auth/`:** Authentication and authorization logic.
    - **`controllers.py`:** API endpoints for authentication.
    - **`models.py`:** SQLAlchemy models for users.
    - **`schemas.py`:** Pydantic schemas for user data.
  - **`captions/`:** Caption submission and retrieval logic.
    - **`controllers.py`:** API endpoints for captions.
    - **`models.py`:** SQLAlchemy models for captions.
    - **`schemas.py`:** Pydantic schemas for captions.
  - **`images/`:** Image management logic.
    - **`controllers.py`:** API endpoints for images.
    - **`models.py`:** SQLAlchemy models for images.
    - **`schemas.py`:** Pydantic schemas for images.
  - **`users/`:** User management logic.
    - **`controllers.py`:** API endpoints for user management.
    - **`models.py`:** SQLAlchemy models for user profiles or additional user data.
    - **`schemas.py`:** Pydantic schemas for user profiles.
  - **`database/`:** Database connection setup.
    - **`database.py`:** SQLAlchemy engine and session setup.
  - **`utils/`:** Utility functions and configurations.
    - **`config.py`:** Configuration settings (e.g., environment variables).
    - **`crud.py`:** Common CRUD operations.
    - **`dependencies.py`:** Dependency injections (e.g., database session).
    - **`utils.py`:** General utility functions.
- **`alembic/` Directory:** Database migration scripts.
  - **`env.py`:** Alembic environment configuration.
  - **`script.py.mako`:** Template for migration scripts.
  - **`versions/`:** Individual migration scripts.
- **`main.py`:** Entry point of the FastAPI application.
- **`.gitignore`:** Specifies files and directories to ignore in Git.
- **`requirements.txt`:** Lists all project dependencies.
- **`pyproject.toml`:** Configuration file for build tools (e.g., isort, black).
- **`isort.cfg`:** Configuration for isort (import sorter).
- **`environment.yml` (optional):** Conda environment configuration.

## Setup and Installation

### Prerequisites

- **Conda:** Ensure Conda is installed on your machine.
- **PostgreSQL:** Install PostgreSQL and set up a database.
- **Git:** Installed and configured with GitHub access.
- **Postman:** For testing API endpoints.

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/photo_caption_contest.git
   cd photo_caption_contest
   ```

2. **Create and Activate Conda Environment:**
   ```bash
   conda create -n photo_caption_env python=3.10
   conda activate photo_caption_env
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database:**
   - Ensure PostgreSQL is running.
   - Create a new PostgreSQL database (e.g., `photo_caption_db`).
   - Set the `DATABASE_URL` environment variable or update it in your `api/utils/config.py`.
     - Example `DATABASE_URL`:
       ```
       postgresql+psycopg2://photo_user:P%40ssw0rd@localhost:5432/photo_caption_db
       ```
     - **Note:** The `%` character in passwords should be URL-encoded as `%25` or properly escaped in `alembic/env.py`.

5. **Run Database Migrations (Using Alembic):**
   ```bash
   alembic upgrade head
   ```

6. **Start the FastAPI Server:**
   ```bash
   uvicorn main:api --reload
   ```

7. **Access Swagger Documentation:**
   - Navigate to `http://localhost:8000/docs` in your browser.

## API Documentation

The API is documented using Swagger UI, automatically integrated with FastAPI. Access the interactive documentation at:

```
http://localhost:8000/docs
```

## Testing

Use **Postman** to test API endpoints. Import the provided Postman collection (if available) or manually create requests based on the Swagger documentation.

## Deployment

The application is deployed on **Render**, making it accessible online. Follow Render's [official documentation](https://render.com/docs) for deployment steps, including setting environment variables and configuring the PostgreSQL database.

## Project Timeline

| **Week** | **Tasks**                                               |
|----------|---------------------------------------------------------|
| **1**    | Project planning and setup, design database schema      |
| **2**    | Implement user registration and authentication          |
| **3**    | Develop image upload and viewing endpoints              |
| **4**    | Implement caption creation and viewing functionality    |
| **5**    | Add like/upvote feature, integrate caching              |
| **6**    | Develop admin features, write Swagger documentation     |
| **7**    | Test endpoints with Postman, optimize database          |
| **8**    | Deploy application to Render, final testing             |

*Adjust the timeline based on your personal schedule and project complexity.*

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

2. **Create a New Branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Commit Your Changes:**
   ```bash
   git commit -m "Add some feature"
   ```

4. **Push to the Branch:**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).