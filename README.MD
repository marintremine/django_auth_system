# Django Authentication System

This project serves as a proof of concept (POC) for building an authentication system using Django, where pages are accessible based on the groups to which a user belongs.

## Introduction

The Django Authentication System with Group Associations provides a starting point for developers who want to quickly set up a web application with a robust and flexible authentication system.

## Features

The Django Authentication System with Group Associations includes the following features:
- Login
- Logout
- Registration
- Password Reset
- Group-based Access Control
- Redirects to the appropriate page based on the user's group

## Getting Started

To get started with the Django Authentication System with Group Associations, follow these steps:

1. Clone the repository to your local machine:

    ```shell
    git clone https://github.com/marintremine/django_auth_system.git
    ```

2. Install the project dependencies:

    ```shell
    cd django_auth_system
    pip install -r requirements.txt
    ```

3. Configure the project settings:

    - Modify the `settings.py` file to suit your project requirements.

4. Run the migrations to create the necessary database tables:

    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the development server:

    ```shell
    python manage.py runserver
    ```

6. Open your web browser and visit `http://localhost:8000` to see the project in action.

## Contributing

Contributions to the Django Authentication System are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's GitHub repository.