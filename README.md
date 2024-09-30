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
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   └── routers/
│       ├── __init__.py
│       ├── auth.py
│       ├── users.py
│       ├── captions.py
│       └── images.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── README.md
├── requirements.txt
└── environment.yml (optional)
```

- **`app/` Directory:** Contains all application logic.
  - **`main.py`:** Entry point of the FastAPI application.
  - **`models.py`:** Database models using SQLAlchemy.
  - **`schemas.py`:** Pydantic schemas for request and response models.
  - **`crud.py`:** CRUD operations interacting with the database.
  - **`database.py`:** Database connection setup using SQLAlchemy.
  - **`dependencies.py`:** Common dependencies like database sessions and authentication.
  - **`routers/` Directory:** Organizes API endpoints.
    - **`auth.py`:** Authentication and authorization endpoints.
    - **`users.py`:** User management endpoints.
    - **`captions.py`:** Caption submission and retrieval endpoints.
    - **`images.py`:** Image management endpoints.
- **`tests/` Directory:** Contains test cases to ensure API functionality.
- **`.gitignore`:** Specifies files and directories to ignore in Git.
- **`requirements.txt`:** Lists all project dependencies.
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
   - Update the `DATABASE_URL` in your `database.py` or set it as an environment variable.

5. **Run Database Migrations (If Using Alembic):**
   ```bash
   alembic upgrade head
   ```

6. **Start the FastAPI Server:**
   ```bash
   uvicorn app.main:app --reload
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

| **Week** | **Tasks**                                          |
|----------|----------------------------------------------------|
| **1**    | Project planning and setup, design database schema |
| **2**    | Implement user registration and authentication     |
| **3**    | Develop image upload and viewing endpoints         |
| **4**    | Implement caption creation and viewing functionality|
| **5**    | Add like/upvote feature, integrate caching         |
| **6**    | Develop admin features, write Swagger documentation|
| **7**    | Test endpoints with Postman, optimize database      |
| **8**    | Deploy application to Render, final testing        |

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