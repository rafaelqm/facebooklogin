# [UserDataByFacebook][docs]


**App to save some user data from Facebook at local database.**

# Requirements

* Python (2.7)
* Django (1.8)
* mysql-python (1.2.5)
* djangorestframework (3.1.3) // REST API
* django-cors-headers (1.1.0) // To allow cross-site requests

# Requirements additionals for Developers

* Coverage (3.7.1)
* Model-mommy (1.2.5)

# Installation

run git clone https://github.com/rafaelqm/facebooklogin.git

Configure the config/settings.py the lines 89 to 98, configuring to your database (you need to create a blank or have one already)

## Warning - There is a file named local_settings.py at config folder, if you are running at local environment, you must edit this file too, otherwise you can just delete it.

run pip install -r requirements.txt // Or install one by one

run python manage.py migrate
Create the user Admin
python manage.py createsuperuser

run python manage.py runserver


Open the admin page
    {{YOUR ADDRESS}}/admin/ 
    LIKE http://127.0.0.1:8000/admin/
 and create a user to use the API
After this go to To Authtoken Module and add one new token, using the user API created before.

Save the token to use at Front (Angular.JS app https://github.com/rafaelqm/facebookloginfront)

# Tests

run 
coverage report
    to see at command line table, or run:
coverage html
    to generate html data from the code coverage of the tests.
# Security

To make the API more secure, go to Settings config/settings.py and set the lines:
    * 76: CORS_ORIGIN_ALLOW_ALL = True // To False and uncomment the lines
    * 82 to 84: And set the url of your front server to allow only calls from it.