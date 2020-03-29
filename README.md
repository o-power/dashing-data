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

Once a user is registered, they are presented with a page to choose their subscription length and then make a payment using Stripe. When a subscription expires, the user will lose their paid access.

<h2 id="demo">Demo</h2>

A live demo of the Dashing Data site can be found [here]() on Heroku.

<h2 id="ux">UX</h2>

### User Stories

- As a **user**, I want to be able to select a chart type.
- As a **user**, I want to be able to upload data for the chart.
- As a **user**, I want to be able to create the chart.
- As a **user**, I want to be able to download an image of the chart.
- As a **user**, I want to be able to save the chart.
- As a **user**, I want to be able to view a list of my saved charts.
- As a **user**, I want to be able to search my saved charts.
- As a **user**, I want to be able to delete a saved chart.
- As a **user**, I want to be able to view a saved chart.
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

**User Model**
| Field | Description |
| :--- | :--- |
| username | Username. Must be unique. |
| email | User's email. Must be unique. |

**UserChart Model**
| Field | Description |
| :--- | :--- |
| user_id | Foreign key to User. Links the chart back to the user. |
| chart_type | Chart type e.g. bar, line. |
| title | Chart title. |
| subtitle | Chart subtitle. |
| date_created | Date chart was saved. |

**BarChart Model**
| Field | Description |
| :--- | :--- |
| chart_id | Foreign key to UserChart. Links the data point back to the chart. |
| x_data | x data point. |
| y_data | y data point. Must be numeric. |

**LineChart Model**
| Field | Description |
| :--- | :--- |
| chart_id | Foreign key to UserChart. Links the data point back to the chart. |
| date_format | Date format e.g. %m-%d-%Y. |
| x_data | x data point. |
| y_data | y data point. Must be numeric. |

**SubscriptionType Model**
| Field | Description |
| :--- | :--- |
| name | Subscription plan name. |
| description | Subscription plan description. |
| length_months | Length of subscription in months. |
| price | Price of subscription in Euro. |

**UserSubscription Model**
| Field | Description |
| :--- | :--- |
| user_id | Foreign Key to User. Links the subscription back to the user. |
| subscription_type_id | Foreign Key to SubscriptionType. Links the subscription back to the subscription type. |
| start_date | Start date of user's subscription. |
| end_date | End date of user's subscription. |
| status | Status of subscription e.g. Active, Expired. |

### Model-View-Template

| App | URL | View | Methods | Template |
| :--- | :--- | :-- | :-- | :-- |
| accounts | accounts/register/ | register | GET, POST | register.html |
| accounts | accounts/profile/ | profile | GET | profile.html |
| accounts | accounts/logout/ | logout | GET | redirect |
| accounts | accounts/login/ | login | GET, POST | login.html |
| accounts | accounts/password-reset/ | PasswordResetView | GET, POST | password_reset_form.html |
| accounts | accounts/password-reset/done/ | PasswordResetDoneView | GET | password_reset_done.html |
| accounts | accounts/password-reset/`<uidb64>`/`<token>`/ | PasswordResetConfirmView | GET, POST | password_reset_confirm.html |
| accounts | accounts/password-reset/complete/ | PasswordResetCompleteView | GET | password_reset_complete.html |
| home | / | index | GET | index.html |
| home | charts/ | create_chart | GET | createchart.html |
| subscription | subscription/ | choose_subscription | GET | subscriptions.html | 
| subscription | subscription/`<int:pk>`/payment/ | pay_subscription | GET, POST | payment.html |
| search | search/charts/ | all_charts | GET | savedcharts.html |
| search | search/result/ | do_search | GET | redirect |
| search | search/save/ | save_chart | GET, POST | redirect |
| search | search/`<int:pk>`/delete/ | delete_chart | GET, POST | confirmdelete.html |
| search | search/`<int:pk>`/view/ | load_chart | GET | redirect |
| barchart | barchart/upload/ | upload_chart | GET, POST | upload.html |
| barchart | barchart/chart/ | create_chart | GET | chart.html |
| barchart | barchart/`<int:pk>`/view/ | view_chart | GET | viewchart.html |
| linechart | linechart/upload/ | upload_chart | GET, POST | upload.html |
| linechart | linechart/chart/ | create_chart | GET | chart.html |
| linechart | linechart/`<int:pk>`/view/ | view_chart | GET | viewchart.html |

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
12. [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) is used to style the Django forms.

<h2 id="features">Features</h2>

### Existing

- The user can login using their username or email. The custom authentication backend is case insensitive and ensures that one user's username cannot match another user's email or vice versa.
- The password reset email comes from the Gmail account noreplydashingdata@gmail.com. The template for the email is in the folder templates/registration (password_reset_email.html, password_reset_subject.txt). The password reset is only sent if the email entered matches that of a registered user. When the app is run locally, the email is printed to the console if the env.py file is found.
- When the user first registers they are directed to the choose subscription plan page. Payment is made via Stripe.
- The user can view their account details, including subscription end date on their profile page.
- If the user has no subscription or their subscription has expired, then a button appears on the profile page to direct them to the choose subscription plan page.
- The user can search all their saved charts.
- The user can delete a chart.
- The user can reload a saved chart.
- The user can upload their own data.
- Form validation ensures the number of y data points must match the number of x data points.
- Form validation prevents non-numeric data being entered for the y data.
- For line charts, form validation prevents non-date data being entered for the x data.
- For line charts, the user can select the format of the dates being entered for the x data.
- The charts are responsive. When the window is resized, the charts are redrawn using the new dimensions. The margins, number of tick marks and gridlines are also responsive.
- The user can download a PNG image of their chart.
- If the user has no subscription or an expired subscription, then they will be redirected to the choose subscription plan page when they try to save the chart.
- If the user has no subscription or an expired subscription, then they will be redirected to the choose subscription plan page when they try to create a paid chart (e.g. line chart).
- If the user has an active subscription and they try to pay for another subscription, the payment will be prevented and the user will be redirected away.
- The admin panel is customized to show the BarChart or LineChart on the same page as the parent model UserChart.
- A custom context processor is used to handle the uploaded data without saving it in a database. The user can only save the data in the database when they have an active subscription.
- The Django messages framework is used to communicate information, warnings and errors to the user.
- The static files are served using Amazon S3.

### Future

- Allow the user to upload data as a CSV file.
- Allow the user to edit saved charts.
- Improve the PNG download by including the title and subtitle in the image.
- Apply debouncing to the responsive D3.js charts to stop them constantly resizing as the window size is reduced. A full description can be found [here](https://ablesense.com/blogs/news/responsive-d3js-charts) [accessed 23rd March 2020].
- Include more chart types (e.g. area chart).
- Include more chart options (e.g. show/hide gridlines, pick colours, show/hide labels, order by, add x and y labels).
- Add pagination to the list of saved charts.

<h2 id="testing">Testing</h2>

Testing cards: https://stripe.com/docs/testing#international-cards

<h2 id="deployment">Deployment</h2>

### Environment Variables

The following environment variables must be set.
| Environment Variable | Description |
| :--- | :--- |
| USE_POSTGRES | If 'TRUE', then the Heroku Postgres database is used. If 'FALSE', then the SQLite development database is used. |
| USE_S3 | If 'TRUE', then static files are served from Amazon S3. If 'FALSE', then static files are served by the Django development server. |
| SECRET_KEY | A secret key for the Django installation. |
| EMAIL_ADDRESS | Address for the email account being used to send the password reset emails, e.g. noreplydashingdata@gmail.com. |
| EMAIL_PASSWORD | Password for the email account being used to send the password reset emails. |
| STRIPE_PUBLISHABLE | Stripe API key. |
| STRIPE_SECRET | Stripe API key. |
| AWS_ACCESS_KEY_ID | Amazon S3 access key id.  |
| AWS_SECRET_ACCESS_KEY | Amazon S3 secret access key. |
| DATABASE_URL | The Postgres database URL generated by Heroku. |
| HOSTNAME | The name of the deployed app, e.g. dashing-data.herokuapp.com. |
| DISABLE_COLLECTSTATIC | Set to 1 to stop Heroku running collectstatic during the deployment as the static files will be served from Amazon S3. This environment variable is not needed for local development. |

### Local Development Environment

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

The Subscription Type values must be entered using the admin panel.

USE_S3 = 'TRUE' then run `python manage.py collectstatic` to collect the static files into the STATIC_URL location (i.e. the S3 bucket).

### Heroku Production Environment

The Subscription Type values must be entered using the admin panel.

<h2 id="credits">Credits</h2>

### Content

- The D3.js code for resizing a chart when the window resizes is adapted from [D3.js Graph Gallery](https://www.d3-graph-gallery.com/graph/custom_responsive.html) [accessed 23rd March 2020].
- Dynamic D3.js left margin adapted from [stackoverflow](https://stackoverflow.com/questions/17109549/set-y-axis-of-d3-chart-to-fit-widest-label) [accessed 27th March 2020].
- Download svg to image functionality taken from [Nikita Rokotyan's Block](http://bl.ocks.org/Rokotyan/0556f8facbaf344507cdc45dc3622177) [accessed 27th March 2020].
- Code for D3.js gridlines adapted from [Sam Hooker's Block](http://bl.ocks.org/35degrees/23873a64ceec2390c400694b6a8b57d9) [accessed 28th March 2020].
- Formatting of messages using bootstrap classes taken from [simpleisbetterthancomplex.com](https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html) [accessed 21st March 2020].
- The Stripe code for accepting a payment was adapted from [Charges API](https://stripe.com/docs/payments/accept-a-payment-charges#web-create-token) [accessed 29th March 2020].

### Media

- The site logo was created using Microsoft PowerPoint.

### Acknowledgements

- The shortcut icon was generated using [Favicon Generator](https://realfavicongenerator.net/) [accessed 21st March 2020].