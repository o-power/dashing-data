<h1 id="title">Dashing Data</h1>

1. [Introduction](#introduction)
2. [Demo](#demo)
3. [UX](#ux)
4. [Technologies/Libraries](#technologies)
5. [Features](#features)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)

<h2 id="introduction">Introduction</h2>

<h2 id="demo">Demo</h2>

A live demo of Dashing Data app can be found [here]() on Heroku.

<h2 id="ux">UX</h2>

### User Stories

### Models

### Navigation

<h2 id="technologies">Technologies/Libraries</h2>

1. [MongoDB](https://www.mongodb.com/) was used as the NoSQL database for the app.
2. [Python](https://www.python.org/) was used as the back-end language.
3. [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) was used as the templating language for rendering the pages.
4. [Materialize](https://materializecss.com/) was used as the front-end framework.
5. Microsoft PowerPoint was used to create the logo.
6. [S3](https://www.gimp.org/) was used to reduce the file size of the background photo and thereby speed up how fast it loads.
7. [Heroku](https://www.heroku.com/) was used to deploy the app.

Fontawesome
Django
Postgres
Heroku
Bootstrap
D3
S3
Gmail

<h2 id="features">Features</h2>

### Existing

### Future

## Local development environment
Clone
Create a virtual environment and activate it
```
python -m venv env
source env/Scripts/activate
```
Install packages from requirements.txt
```
pip install -r requirements.txt
```
Create an env.py file (need a stripe account and test api keys)
Makemigrations
Migrate

## Password reset

The password reset email comes from the Gmail account noreplydashingdata@gmail.com. When the app is ran locally, the email is printed to the console if the env.py file is found.

The template for the email is in the folder templates/registration.
password_reset_email.html
password_reset_subject.txt

The passowrd email is only sent if the email exists for a registered user.

## Subscriptions

The subscription types are added/edited in the admin panel.

Testing cards: https://stripe.com/docs/testing#international-cards
Stripe Charge instructions: https://stripe.com/docs/payments/accept-a-payment-charges#web-create-token

Screenshot of Stripe dashboard.

## Adding a new chart type

<h2 id="testing">Testing</h2>

<h2 id="deployment">Deployment</h2>

Heroku
Disable the collectstatic build step which Heroku runs on your behalf:
DISABLE_COLLECTSTATIC = 1

Django deployment checklist
https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

<h2 id="credits">Credits</h2>

### Content
- Formatting of messages using bootstrap classes taken from [simpleisbetterthancomplex.com](https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html) [accessed 21st March 2020].

### Media
- The site logo was created using Microsoft PowerPoint.

### Acknowledgements
- The shortcut icon was generated using [Favicon Generator](https://realfavicongenerator.net/) [accessed 21st March 2020].