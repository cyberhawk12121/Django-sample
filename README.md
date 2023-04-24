# Django-sample
Django authentication and the content posting functionality.

* Installing Django and running the code: To install Django make sure pip is installed. After that step go ahead and write following in the terminal "pip install django". 
This will download and intall the django latest version. After this step now go to the directory in which this django code is placed. Type the following command next: 
  - python manage.py makemigrations 
  - python manage.py migrate 
  - python manage.py runserver Now, after the final command the server will start running and notice that in the app directory there will be migrations files that are now created. Run any browser and go to the 127.0.0.1:8000/ or the any other port number allocated. The page will surely load.

* URLs: 
  1. 127.0.0.1:8000/login : This is for the user login page 
  2. 127.0.0.1:8000/register: This is for the user registration page
  3. 127.0.0.1:8000/ : This is the Home page
  4. 127.0.0.1:8000/post/create : This is restricted for only authenticated users and used to create authenticated users.
  5. 127.0.0.1:8000/post/postlist : Shows the list of posts
  6. 127.0.0.1:8000/post/<slug> : It shows a particular post
  7. 127.0.0.1:8000/post/<slug>/like: It will allow user to like that particular post

* Methods and Classes: All the methods and classes are written inside the views.py which renders the templates as well as performs basic queries on the database too. We can say it's the heart of the project. Read more here: https://docs.djangoproject.com/en/3.0/topics/http/views/

* URL's in the project: Every URL is mapped to a view method or class, like so: path(, <method_name/class_name>, ). For each URL path on goes to, a view method is triggered which renders the corresponding HTML page. Read more here: https://docs.djangoproject.com/en/3.0/topics/http/urls/

* How it achieves custom user authentication? It uses a custom user model(inside models.py) as opposed to the base "User" model provided by Django. The class AbstractBaseUser has been extended and changes are made into it. Originally usernames is used to signup a user but here "email" is taken for this process. Read more here: https://docs.djangoproject.com/en/3.0/ref/contrib/auth/

* Django templating: The Django template language is Django’s own template system. Until Django 1.8 it was the only built-in option available. It’s a good template library even though it’s fairly opinionated and sports a few idiosyncrasies. If you don’t have a pressing reason to choose another backend, you should use the DTL, especially if you’re writing a pluggable application and you intend to distribute templates. In a nutshell it allows to run django code inside the HTML pages. Read more here: https://docs.djangoproject.com/en/3.0/topics/templates/

* Django Database api: Django automatically gives you a database-abstraction API that lets you create, retrieve, update and delete objects. An example that has been used in the project is .objects.all(). This fetches the entire instance of the model. Read more here: https://docs.djangoproject.com/en/3.0/topics/db/queries/

> Footnote: The project uses Django version 3.0 - install pillow for including images in the models (write "pip install pillow" in the terminal).
