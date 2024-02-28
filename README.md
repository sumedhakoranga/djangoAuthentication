# Overview of the User Registration Application

**Application Framework and Language**
  - Framework: Django
  - Programming Language: Python
    
**Database Management**
  - Database System: SQLite
    
**Major Documentation used**
  - https://developers.google.com/gmail/api/guides/sending
  - https://developers.google.com/gmail/api/quickstart/python

## Installation

  - Follow [this](https://developers.google.com/gmail/api/quickstart/python) documentation to create your own ```crendetial.json``` and ```credential.env```
  -  Clone the repository and run the following commands

```bash
    python3 -m venv django_project
    source django_project/bin/activate
    pip install django
    django-admin startproject django_project
    python manage.py migrate
    python manage.py runserver  
```

## User Registration Process

**The user registration process involves several key steps:**

  - User Form Submission: Users submit their registration details via a form, including username, email, and password.

  - Data Validation: The application checks that all fields are filled with valid information. It also verifies that the user's email does not already exist in the database to prevent duplicate registrations.

  - Database Storage: Upon successful validation, the user's information is stored in the SQLite database.

## Email Verification System

  - Email Service: Gmail API
     - The application uses Gmail API as the email service provider to verify each user's email address.
  - Verification Method: Unique Verification Token
     - Unique verification tokens are generated using the UUID library, and this token is sent to the user’s email address as part of the verification link.

## Steps for Email Verification:

  - Token Generation: UUID generates A unique token for each user.

  - Email Composition: An email containing the verification link with the embedded token is prepared.

  - User Verification: Users click the verification link, which leads them to a verification page within the application. The application validates the token and activates the user's account upon successful verification.

## Security Measures

  - Password Hashing: User passwords are hashed using Django's built-in authentication system to ensure security.

  - Token Security: UUID provides a secure and unique token for each user, minimizing the risk of unauthorized access.

## Conclusion

The Django user registration application efficiently handles user registration, data storage, and email verification. The application ensures a seamless and secure user registration process by leveraging SQLite for database management, Google Email for email verification, and UUID for secure token generation.
