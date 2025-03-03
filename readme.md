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

   ```JSON
   virtualenv env
   env\scripts\activate
   ```

5. Install the project dependencies

```JSON
pip install django djangorestframework djangorestframework-simplejwt
```

6. Run the project

## API Usage

To use this project API :

1. Authentication - Register

   ```JSON
   http://127.0.0.1:8000/api/auth/register/
   ```

   - Json:
     ```JSON
      "name": "User 1",
      "email": "user1@example.com",
      "password": "U1@123456"
     ```

   ```JSON
   password contains 8 characters
   ```

2. Authentication :- Login

   ```JSON
   http://127.0.0.1:8000/api/auth/login/
   ```

   - Json:

     ```JSON
      "email": "user1@example.com",
      "password": "U1@123456"
     ```

   - response

     ```JSON
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
   ```JSON
    http://127.0.0.1:8000/api/user/profile/10/
   ```
   10 is your profile user id

PUT : edit profile by using form-data not json

```JSON
   http://127.0.0.1:8000/api/user/profile/10/
```

4. Courses :
   category : use access token for details
   GET:
   ```JSON
    http://127.0.0.1:8000/api/courses/categories
   ```

GET : fetch all the courses (show only 10)

```JSON
   http://127.0.0.1:8000/api/courses?limit=10
```

5. Courses Enroll :
   category : use access token for details
   Post:

   ```JSON
    http://127.0.0.1:8000/api/courses/enroll/
   ```

   Json:

   ```json
   {
     "course_id": 4,
     "confirm": true
   }
   ```

6. Courses Enroll :
   category : use access token for details
   Post:

   ```JSON
    http://127.0.0.1:8000/api/courses/enroll/
   ```

   Json:

   ```json
   {
     "course_id": 4,
     "confirm": true
   }
   ```

7. Tips : courses me hai 
   category : use access token not required
   GET:

   ```JSON
    http://127.0.0.1:8000//api/tips/
   ```

<!-- 8. Help / FAQs :
   category : use access token Not required
   GET:

   ```JSON
    http://127.0.0.1:8000/api/help/FAQ/
   ```

9. Help / ASK Question :
   category : use access token required
   Post:

   ```json
    http://127.0.0.1:8000/api/help/ask/
   ```

   JSON:

   ```json
   {
   "question": "How can i Joined Courses"
   }
   ```

   10. Help / user- Question :
   category : use access token required
   user can see the answer of the asked question 

   GET:

   ```json
    http://127.0.0.1:8000//api/help/user-questions/
   ```

   JSON:

   ```json
   {
   "question": "How can i Joined Courses"
   }
   ```
   
 -->
