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

Dashing Data is a website which allows users to create charts from their own data. Users can create bar charts for free but a subscription must be paid in order to create other chart types (e.g. line chart) or to save charts.

Once a user is registered, they are presented with a page to choose their subscription length and then make a payment using Stripe. When a subscription expires, the user will lose their premium access.

<h2 id="demo">Demo</h2>

A live demo of Dashing Data site can be found [here]() on Heroku.

<h2 id="ux">UX</h2>

### User Stories

- As a **user**, I want to be able to select a chart type.
- As a **user**, I want to be able to upload my own data for the chart.
- As a **user**, I want to be able to view the chart.
- As a **user**, I want to be able to save my chart.
- As a **user**, I want to be able to view a list of my saved charts.
- As a **user**, I want to be able to search my saved charts.
- As a **user**, I want to be able to delete a saved chart.
- As a **user**, I want to be able to choose a subscription length.
- As a **user**, I want to be able to pay the subscription fee.
- As a **user**, I want to be able to view my profile.
- As a **user**, I want to be able to register.
- As a **user**, I want to be able to log in using my email or username.
- As a **user**, I want to be able to log out.
- As a **user**, I want to be able to reset my password by email.
- As a **user**, I want the site and charts to be responsive so that I can use the site on any device.
- As a **site owner**, I want to restrict users access if they don't have an active subscription.
- As a **site owner**, I want to be able to use the admin panel to manage content on the site.
- As a **site owner**, I want validation on the data upload to ensure the data has the correct data types.
- As a **site owner**, I want continuous integration testing to ensure that code changes do not break existing features.

### Models

| Model | Description |
| :--- | :--- |
| User | Django user model. Each row represents a registered user. |
| UserChart | Each row represents a chart that the user has saved. |
| BarChart | Each row represents a row of data for a bar chart that the user has saved. |
| LineChart | Each row represents a row of data for a line chart that the user has saved. |
| SubscriptionType | Contains the subscription types that the user can choose from. |
| UserSubscription | Each row represents a user subscription. |

User Model
| Field | Description |
| :--- | :--- |
| username | Username. Must be unique. |
| email | User's email. Must be unique. |

UserChart Model
| Field | Description |
| :--- | :--- |
| user_id | Foreign key to User. Links the chart back to the user. |
| chart_type | Chart type e.g. bar, line. |
| title | Chart title. |
| subtitle | Chart subtitle. |
| date_created | Date chart was saved. |

BarChart Model
| Field | Description |
| :--- | :--- |
| chart_id | Foreign key to UserChart. Links the data point back to the chart. |
| x_data | x data point. |
| y_data | y data point. Must be numeric. |

LineChart Model
| Field | Description |
| :--- | :--- |
| chart_id | Foreign key to UserChart. Links the data point back to the chart. |
| date_format | Date format e.g. %m-%d-%Y. |
| x_data | x data point. |
| y_data | y data point. Must be numeric. |

SubscriptionType Model
| Field | Description |
| :--- | :--- |
| name | Subscription plan name. |
| description | Subscription plan description. |
| length_months | Length of subscription in months. |
| price | Price of subscription in Euro. |

UserSubscription Model
| Field | Description |
| :--- | :--- |
| user_id | Foreign Key to User. Links the subscription back to the user. |
| subscription_type_id | Foreign Key to SubscriptionType. Links the subscription back to the subscription type. |
| start_date | Start date of user's subscription. |
| end_date | End date of user's subscription.. |
| status | Status of subscription e.g. Active, Expired. |

### Navigation

| App | URL | View | Methods | Template |
| :--- | :--- | :-- | :-- | :-- |
| accounts | register/ | register | GET, POST | register.html |
| accounts | profile/ | profile | GET | profile.html |
| accounts | logout/ | logout | GET |  |
| accounts | login/ | login | GET, POST | login.html |
| subscription | / | choose_subscription | GET | subscriptions.html | 
| subscription | `<int:pk>`/payment/ | pay_subscription | GET, POST | payment.html | 
| accounts | password-reset/ | PasswordResetView | GET, POST | password_reset_form.html |
| accounts | password-reset/done/ | PasswordResetDoneView | GET | password_reset_done.html |
| accounts | password-reset/`<uidb64>`/`<token>`/ | PasswordResetConfirmView | GET, POST | password_reset_confirm.html |
| accounts | password-reset/complete/ | PasswordResetCompleteView | GET | password_reset_complete.html |

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
- Code for D3.js gridlines adapted from [Sam Hooker's Block](http://bl.ocks.org/35degrees/23873a64ceec2390c400694b6a8b57d9) [accessed 28th March 2020].
- Formatting of messages using bootstrap classes taken from [simpleisbetterthancomplex.com](https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html) [accessed 21st March 2020].

### Media
- The site logo was created using Microsoft PowerPoint.

### Acknowledgements
- The shortcut icon was generated using [Favicon Generator](https://realfavicongenerator.net/) [accessed 21st March 2020].