# Flask App Skeleton
Skeleton flask python application provided by [Carlos Castillo](http://github.com/carloscastillo10) is a project that could help beginners to quickly have a simple structure of a python-based project using the Flask framework.

![image](https://user-images.githubusercontent.com/38107722/156813966-d61ebf15-a221-49c8-88ef-f7d281694e47.png)
--

## How to use it
```
$ # Use the template
$ Select the option of <Use this template >
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env -p python3
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env -p python3
$ # .\env\Scripts\activate
$
$ # Install requirements
$ pip3 install -r requirements.txt
$
$ # Set the FLASK_APP configuration
$ (Unix/Mac) . unix_configuration.sh
$ (Windows) windows_configuration.bat
$
$ # Start the application (development mode)
$ flask run
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
```
---
## Code-Base structure
The project is coded using blueprints, app factory pattern, dual configuration profile (development and production) and an intuitive structure presented bellow:


```bash
< PROJECT ROOT >
   |
   |-- app/
   |    |-- base/                                # Base Blueprint - serve app pages
   |         |-- static/
   |         |    |-- <css, JS, images>          # CSS files, Javascripts files
   |         |
   |         |-- templates/                      # Templates used to render pages
   |              |-- base.html                  # Used by common pages
   |              |-- index.html                 # Default page
   |
   |         |-- __init__.py                     # Initialize the blueprint
   |         |-- routes.py                       # App pages routes
   |    |
   |    |-- __init__.py                          # Initialize the app
   |    |-- config.py                            # Set up the app
   |
   |-- unix_configuration.sh                     # Set application configuration on Unix-based systems
   |-- windows_configuration.bat                 # Set application configuration on Windows-based systems
   |-- requirements.txt                          # Development modules 
   |-- run.py                                    # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```
