# Django files description

## Project structure
Here is a representation of the files structure:
```
📦hillel_05_2022_support
 ┣ 📂authentication
 ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┗ 📜views.py
 ┣ 📂config
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜wsgi.py
 ┣ 📂core
 ┃ ┣ 📂api
 ┃ ┃ ┣ 📜exchange_rate.py
 ┃ ┃ ┗ 📜tickets.py
 ┃ ┣ 📂migrations
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┗ 📜views.py
 ┣ 📂docs
 ┃ ┣ 📜car_service_db.png
 ┃ ┗ 📜social_network_db.png
 ┣ 📂shared
 ┃ ┣ 📂django
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜models.py
 ┃ ┗ 📜__init__.py
 ┣ 📜.flake8
 ┣ 📜.gitignore
 ┣ 📜.isort.cfg
 ┣ 📜Pipfile
 ┣ 📜Pipfile.lock
 ┗ 📜manage.py
```
------

# Directories 

## Config directory

In this directory, we store all main settings and configuration files for our project.

## 'Authentication' directory

We created separate apps for real logical part of our project - using devisional structure of a project.

**Authentication** directory as a subprogram is responsible for user signin, signin, signout etc.

## 'Core' directory

The **Core** directory will be responsible for the main logic of the project.

## 'Shared' directory
We created this directory to store files,libraries, functions, etc that we may use inside our apps/project.


# Files

**Manage.py** This file is used as a command line utility for our project. We use this file to debug, deploy and run our web app.

**settings.py** - main configuration file, that contains all configurations of Django project. Such as variables, modules, using apps, etc.

**urls.py** - main routing file. This file we use for creating entry points (urls).

**wsgi.py** - this file we will use this file for production. WSGI stands for Web Server Gateway Interface.

**asgi.py** - as I understand, it's similar to wsgi but with additional functional (like async functional)

**admin.py** - this file need for register and representation of our app's models inside Django admin panel.

 **\_init\_.py** - this file tells python that this directory can be used as a package.

 **models.py** - insode this file we write a representation of the models in the form of classes and define the structure of the database.

 **view.py** - this file defines how the user will interact with our app. Here we have the logic of how we will respond on user requests.

 **tests.py** - for writing tests for the app. 

 **apps.py** - have no idea. On the internet, I found it's needed to configure our app's attributes.

 **migrations directory / files** -  here django creates files that has step-by-step instructions for creating and changing our database.

------

## Other utilits

**Pipfile** - this file contains information for the dependencies of the project. Pipenv uses this file to define all required tools, utils, and modules for this env.  Here we separate dev packages and default so that we can use this file for dev and prod. 

**Pipfile.lock** - This file declares all dependencies (from Pipfile) of the project, their latest available versions, and the current hashes for the downloaded files. 

**.isort.cfg** - we use this file to configure isort behavior. In my case, I exclude migrations from the checking.

**.flake8** - we use this file to configure flake8 behavior.

**.gitignore** - here we specifie files that git shoud ignore.

---

## External tools

For CI/CD:
- isort
- black
- flake8