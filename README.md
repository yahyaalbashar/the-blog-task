# the-blog-task
## Intro
  this is a blog web app built with django 2.2, it allows users to create, list, update and delete blog articles. also it allows them to like articles.
  This app also uses django rest framework for API's to be consumed by clients.
## runnig the app
  to get this app running on your machine follow below steps:
  - this app requires python 3.6 to be installed on your machine make sure to install it
  - install vertualenv or pipenv for virtual environment
  - open terminal/command-line and cd to theblog directory
  - after activating the virtual environment  run the command pip install -r requirements.txt to install the required packages for this app which are:
    - django 2.2
    - sendgrid
  - run the command python manage.py makemigrations to read the migrations
  - run the command python manage.py migrate to apply migrations
  - create superuser with the command python manage.py createsuperuser and follow the prompts for email and password 
  - run the server via command python manage.py runserver
## Important for sendgrid:
  sendgrid is cloud-based email delivery platform. you have to have an account and an API key (Important) please register [here](https://signup.sendgrid.com/).
  after getting your API key, open theblog/utils.py file and place your API key or see how to create a enviornment variable see [here](https://app.sendgrid.com/guide/integrate/langs/python).
  in the project settings.py file set the sender email and reciever email to send an email to the admin on every article liked by a user:
#### SENDER_EMAIL='yoursender@email.com'
#### RECIEVER_EMAIL='yourreciever@email.com'

# usage from browser:
go to http://127.0.0.1:8000/admin/login to login
from there you can create articles, categories, add users and groups

visit http://127.0.0.1:8000/ for home page to see listed articles

# API's:
endpoint|Description 
 ------------- | -------------
GET api/list-articles/ | returns a list of articles created by users, you can send a 'query' param with a desired value to search article title,content or author name
GET api/get-article/:id/ | returns a single article
GET api/:id/like/ | adds a like by an authenticated user.for the browser version session authentication is used, for api testing tools such as postman; basic authentication is used.
