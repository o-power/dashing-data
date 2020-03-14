# Dashing Data

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

## Subscriptions

The subscription types are added/edited in the admin panel.

Testing cards: https://stripe.com/docs/testing#international-cards
Stripe Charge instructions: https://stripe.com/docs/payments/accept-a-payment-charges#web-create-token

Screenshot of Stripe dashboard.

## Credits

Formatting of messages https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html