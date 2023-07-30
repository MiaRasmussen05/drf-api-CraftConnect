# Craft|Hub Backend

Welcome to Craft|Hub! This website was made for my last project with Code Institute for my React project. DIY is only getting bigger by the minute and that is what Craft|Hub is all about. To connect, share, inspire. Learn from others and share your own experinces. Follow your favorite users or your friends. Keep an eye out on events. Make your own list to never forget your DIY ideas and get started on them. Comment and like posts and be apart of community.

[Link to live side on Heroku](https://craftconnect-6c932655ea4f.herokuapp.com/)

[Link to live side fpr the API on Heroku](https://drf-api-crafthub-d1d89ee1951b.herokuapp.com/)

![GitHub shield last commit](https://img.shields.io/github/last-commit/MiaRasmussen05/drf-api-CraftConnect?color=red)
![GitHub shield language count](https://img.shields.io/github/languages/count/MiaRasmussen05/drf-api-CraftConnect?color=orange)
![GitHub shield contributors](https://img.shields.io/github/contributors/MiaRasmussen05/drf-api-CraftConnect?color=yellow)
![GitHub shield top language](https://img.shields.io/github/languages/top/MiaRasmussen05/drf-api-CraftConnect?color=brightgree&label=html)

# Table of Contents

[Overview](#overview) 

[User Stories](#user-stories)

[Database Schema](#database-schema)

[Technology](#technology)
- [Languages Used](#languages-used)
- [Libraries and Programs Used](#libraries-and-programs-used)

[Testing](#testing)
- [Automated Testing](#automated-testing)
- [Manual Test Cases](#manual-test-cases)
- [Code Validation](#code-validation)
- [Bugs](#bugs)

[Deployment](#deployment)

[Requirements](#deployment)

[Credits](#credits)
- [Resources Used](#resources-used)
- [Content](#content)
- [Honourable mentions](#honourable-mentions)

# Overview

This site was developed because of my love creating. I do it on a daily base from baking to coding and everything in between. So to get more people out there and get them into DIY and learning from others I have created this site.

# User Stories
All the user stories where managed in the Kanban board which was created inside GitHub Projects. User stories were then prioritized with the MoSCoW approach and the labels on the Kanban board where used to manage this. The Kanban board was split into three columns to manage the various stages of development:

  1. To do: This item hasn't been started yet.
  2. In Progress: This item is actively being worked on in the Backend and Frontend.
  3. Done: All tasks have been completed.

# __Databases__

  Data normalisation to structure each model to help reduce data redundancy and improve data integrity. This was used after setting out all of the information required for the site.

  ![Databases](https://imgur.com/LlYfNNi.png)

# Technology

 ## Languages Used

  - Python
  - SQL (Postgres)

  ## Libraries and Programs Used

  - __Git__ - Was used for version control, the Gitpod terminal to commit and push to GitHub.
  - __GitHub__ - Was used to store the project code and display the project in GitHub Pages.
  - __Heroku__: Where used for Deployment.
  - __Cloudinary__: Where used to save static media files.
  - __ElephantSQL__: Where used for PostgreSQL database hosting.
  - __Django/Django REST Framework__: Where used for Backend database and API.
  - __Google Chrome, Microsoft Edge, Mozilla Firefox, Safari__: Where all used for site testing - on alternative browsers.
  - __Chrome Dev Tools__: Were used to test and troubleshoot the webpage as well as fix problems with responsive design and styling.

# Testing

  ## Manual Test Cases

  ## Code Validation

  - CI Python Linter: No errors were found when passing through the CI Python Linter. And only a warnings for lines that where to long came up.

  ## Bugs

  There were no unfixed bugs.

# Deployment

  __Create Database__

  1. In ElepahantSQL, click "Create New instance" button.
  2. Set up the Tiny Turtle plan, and then select the nearest datacenter to you and click the "Review" button.
  3. Copy the new DATABASE_URL.

  __Connect Cloudinary__

  1. In the terminal: install dj-cloudinary-storage.
  2. And then add CLOUDINARY_URL to the env.py file.
  3. In the settings.py, update the apps to include cloudinary-storage.
  4. Below the import statements in settings, add the following variables for Cloudinary:
```
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.ger('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinartStorage'
```
  5. Below INSTALLED_APPS in settings, set site ID:
```
SITE_ID = 1
```

  __Create the Heroku App__

  1. On the Heroku dashboard, click the "Create a new app" button.
  2. Go to the config vars in settings and copy paste in the new DATABASE_URL and CLOUDINARY_URL.

  __Connect Project to ElepahantSQL__

  1. In the terminal: install dj_database_url and psycopg2.
  2. In settings.py: import dj-database_url and import os.
  3. Now updated the DATABASES variable to:
```
DATABASES = {
    'default': ({
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
    )
}
```
  4. Add in the env.py:  
  5. os.environ.setdefault("DATABASE_URL", "<your PostgreSQL URL here>")
  6. Temporarily comment out the environment variable to connect gitpod to your external database.
  7. In ElepahantSQL browser, check if the database is now connected.
  8. If connected, migrate the database and then create a superuser.

  __Deploy on Heroku__

  *In gitpod workspace*

  1. In the terminal, install gunicorn.
  2. Remeber to update the requirements.txt file.
  3. Now create the Procfile.
  4. In settings.py 

   - Add the Heroku app to the ALLOWED_HOSTS variable:
    ```
    os.environ.get('ALLOWED_HOST'),
    'localhost',
    ``` 
    - Add corsheaders to INSTALLED_APPS
    - Add corsheaders middleware to the top of MIDDLEWARE:
  ```
  'corsheaders.middleware.CorsMiddleware',
  ```
- Set ALLOWED_ORIGIN to make network requests
- Below BASE_DIR, create the REST_FRAMEWORK, and include page pagination to improve app loading times, pagination count, and date/time format:
  ```
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [(
          'rest_framework.authentication.SessionAuthentication'
          if 'DEV' in os.environ
          else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
      )],
      'DEFAULT_PAGINATION_CLASS':
          'rest_framework.pagination.PageNumberPagination',
      'PAGE_SIZE': 10,
      'DATETIME_FORMAT': '%d %b %Y',
  }
  ```
    - Set the default renderer to JSON:
  ```
  if 'DEV' not in os.environ:
      REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
          'rest_framework.renderers.JSONRenderer',
      ]
  ```
    - Add the following, setting the JWT_AUTH_SAMESITE to 'None'
  ```
  REST_USE_JWT = True
  JWT_AUTH_SECURE = True
  JWT_AUTH_COOKIE = 'my-app-auth'
  JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
  JWT_AUTH_SAMESITE = 'None'
  ```
    - Remove the value for SECRET_KEY and replace with: SECRET_KEY = os.getenv('SECRET_KEY')
    - Below ALLOWED_HOST, added the CORS_ALLOWED variable.
  ```
  if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

  if 'CLIENT_ORIGIN_DEV' in os.environ:
      extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
      CORS_ALLOWED_ORIGIN_REGEXES = [
          rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
      ]
  ```
    - Set the debug value to True if the DEV environment variable exists:
  ```
  DEBUG = 'DEV' in os.environ
  ```

  5. In env.py
  - Add SECRET_KEY
  - Comment DEV back in 
  6. Update the requirements.txt file
  7. Migrate the database
  8. Add, commit and push the code to github 

  *In Heroku*
  1. Add SECRET_KEY, ALLOWED_HOST, CLIENT_ORIGIN and CLIENT_ORIGIN_DEV to the config vars
  2. Then manually re-deploy the app to github.

# Requirements

  - asgiref==3.7.2
  - cloudinary==1.33.0
  - dj-database-url==0.5.0
  - dj-rest-auth==2.1.9
  - Django==3.2.20
  - django-allauth==0.44.0
  - django-cloudinary-storage==0.3.0
  - django-cors-headers==4.2.0
  - django-filter==23.2
  - djangorestframework==3.14.0
  - djangorestframework-simplejwt==5.2.2
  - gunicorn==20.1.0
  - oauthlib==3.2.2
  - Pillow==10.0.0
  - psycopg2==2.9.6
  - PyJWT==2.7.0
  - python3-openid==3.2.0
  - pytz==2023.3
  - requests-oauthlib==1.3.1
  - sqlparse==0.4.4

# Credits

  ## Resources Used

  - Code Institutes 'Django Rest Framework Walkthrough Videos'
  - Code Institutes 'Moments Walkthrough Videos'
  - React Bootstrap documentation
  - W3C Schools 
  - Stack Overflow for enquiries relating to React.js.
  - Slack

  ## Honourable mentions

  - My mentor Rohit for the support and helping me understand what I needed to do.
  - All my favorite people that have gone through and tested my site whenever I asked.
  - Martin CI Tutor for helping me find out my config vars need to be updated.
  - Rebecca CI Tutor for going over 404 error for problems in my settings file for my deployed DRF API.