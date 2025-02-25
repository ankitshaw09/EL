<!-- create a virtual environment  -->

# E-Learning app

## Description

This is a project description.

## Installation

To install this project, follow these steps:

1. Clone the repository
2. Navigate to the project directory
3. Download Virtual Environment

   ```
   pip install virtualenv
   ```

4. Create a virtual environment using the command:

   ```bash
   virtualenv env
   env\scripts\activate
   ```

5. Install the project dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

6. Run the project

## API Usage

To use this project API :

1. Authentication - Register

   ```bash
   http://127.0.0.1:8000/api/auth/register/
   ```

   - Json:
     ```bash
      "name": "User 1",
      "email": "user1@example.com",
      "password": "U1@123456"
     ```

   ```bash
   password contains 8 characters
   ```

2. Authentication :- Login

   ```bash
   http://127.0.0.1:8000/api/auth/login/
   ```

   - Json:

     ```bash
      "email": "user1@example.com",
      "password": "U1@123456"
     ```

   - response

     ```bash
           {
              "user": {
                       "id": 2,
                       "email": "user2@example.com",
                       "name": "User 2",
                       "is_staff": false,
                       "is_active": true
                    },
              "access_token":"eyJhbGciOWNjZXNzIiwiZXhwIjoxNzM5OTYzOTM3LC",

              "refresh_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
           }

     ```

3. Profile : use access token for details
   GET:
   ```bash
    http://127.0.0.1:8000/api/user/profile/10/
   ```
   10 is your profile user id

PUT : edit profile by using form-data not json 

   ```bash
      http://127.0.0.1:8000/api/user/profile/10/
   ```


4. Courses :
 category : use access token for details
   GET:
   ```bash
    http://127.0.0.1:8000/api/courses/categories
   ```
   
GET :  fetch all the courses  (show only 10)

   ```bash
      http://127.0.0.1:8000/api/courses?limit=10
   ```
