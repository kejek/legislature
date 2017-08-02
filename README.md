# Checkout Board

Checkout Board for the Legislative Branch. Used to track employee status in the branch.

## Getting Started

Download the entire contents of checkout_board to local machine.
Using CMD on terminal navigate to the base directory (checkout_board) and use "python manage.py runserver" to run the application.
See deployment for notes on how to deploy the project on a live system.

### Prerequisites/Installing

Checkout Board requires Python 2.7.13 and Django 1.8.7. Python can be install from http://www.python.org and Django can be installed by using "pip install Django==1.8.7" after installing Python.
The checkout board also uses TinyMCE for another process - posting updates to the home page. Which may or may not be used in the final product. Microsoft SQL Client is also required to use the SQL database
server connections. You can also use SQL lite, but would have to change the database under settings. Python LDAP is also required - Installing in a windows environment can be difficult, but a wheel can be found via:
1.	Download python-ldap wheel file from
http://www.lfd.uci.edu/~gohlke/pythonlibs/#python-ldap
2.	Use pip install <location of downloaded wheel file>
e.g. pip install /c/Users/cl0058/Downloads/python_ldap-2.4.41-cp27-cp27m-win_amd64.whl


```
https://www.python.org/downloads/release/python-2713/ for windows
"yum install python27" for Redhat
"pip install Django==1.8.7"

```
## Deployment

Deploying to a live production environment requires some changes to checkout_board/checkout_board/settings.py including changing DEBUG=True to DEBUG=False. Updating the email server and secret_key if needed.

## Built With

* [Django](https://www.djangoproject.com/) - Web Framework
* [Python](https://www.python.org/) - Development Language

## Authors

* **Matt Goldsworthy** - *Initial work*


## Acknowledgments


