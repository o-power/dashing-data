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

1. [Django](https://www.djangoproject.com/) is the backend framework.
2. [Python](https://www.python.org/) is the backend language.
3. [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) is the templating language for rendering the pages.
4. [Bootstrap](https://getbootstrap.com/) is the frontend CSS framework.
5. [Amazon S3](https://aws.amazon.com/) is used to serve the static and media files in production.
6. [Heroku](https://www.heroku.com/) is used to deploy the app.
7. [Font Awesome 4](https://fontawesome.com/v4.7.0/) is used for the icons.
8. [Google Fonts](https://fonts.google.com/) is used for the Roboto font.
9. [D3.js](https://d3js.org/) is used for creating the charts.
10. [Gmail](https://www.google.com/) is used for sending the password resets.
11. [PostgreSQL](https://www.postgresql.org/) is used for the production database.

<h2 id="features">Features</h2>

### Existing

### Future
- Apply debouncing to the responsive D3.js charts to stop them constantly resizing as the window size is reduced. A full description can be found [here](https://ablesense.com/blogs/news/responsive-d3js-charts) [accessed 23rd March 2020].

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

USE_S3
SECRET_KEY
EMAIL_ADDRESS
EMAIL_PASSWORD
STRIPE_PUBLISHABLE
STRIPE_SECRET
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
DATABASE_URL
HOSTNAME


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
- Responsive D3.js code adapted from [D3.js Graph Gallery](https://www.d3-graph-gallery.com/graph/custom_responsive.html) [accessed 23rd March 2020].
- Dynamic D3.js left margin adapted from [stackoverflow](// https://stackoverflow.com/questions/17109549/set-y-axis-of-d3-chart-to-fit-widest-label) [accessed 27th March 2020].
- Download svg to image functionality taken from [Nikita Rokotyan's Block](http://bl.ocks.org/Rokotyan/0556f8facbaf344507cdc45dc3622177) [accessed 27th March 2020].
- Formatting of messages using bootstrap classes taken from [simpleisbetterthancomplex.com](https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html) [accessed 21st March 2020].

### Media
- The site logo was created using Microsoft PowerPoint.

### Acknowledgements
- The shortcut icon was generated using [Favicon Generator](https://realfavicongenerator.net/) [accessed 21st March 2020].