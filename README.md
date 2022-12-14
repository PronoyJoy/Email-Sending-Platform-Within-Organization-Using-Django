# Email Sending [ Django, Boostrap]

# Url - [RomatoProject](http://pronoy242.pythonanywhere.com/)

Feature -

* As a user, I want to sign up with my first name, last name, new email, and password.

* The email address must be unique.

* As a user, I want to sign in using my email address and password.

* As a user, I want to send emails to another email address.

* As a user, I want to receive emails from another email address.

* As a user, I want to get emails in my inbox in four categories:

Primary, Social, Promotional, and Forum.



## Installation

Install this project with this steps -
* Install Django

```bash
  pip install django
```

* Create And Virtual Environment

```bash
  py -m venv venv
  venv\Scripts.activate.bat
```

* Install Required Files
 
```bash
  pip install -r requirements.txt
```

* Migrate Database
 
```bash
  python3 manage.py migrate 
  or
  py manage.py migrate
```

* Create SuperUser fro accessing Django-Admin
```bash
  python3 manage.py createsuperuser
```

* Runserver

```bash
  py manage.py runserver
```



## Deployment

To deploy this project - 

* Git Clone

```bash
$ git clone https://gitlab.com/pdas151242/romatoproject.git

```

* Create Virtual Environment [same as Installtion Process ]

* Install Requirements [ same command as Installation Process ]

* Migrate Database And Createsuperuser[ same as Installation Process ]

* create web project in the deployment site
* select python 3 version
* set project directory to the web project
* set virtual environment directory to the web project
* Change in wsgi.py file [pythonanywhere.com]
```bash
# add your project directory to the sys.path
project_home = '/home/Pronoy242/romatoproject/romatoproject'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'romatoproject.settings'
```
