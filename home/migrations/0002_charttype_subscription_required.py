# Generated by Django 3.0.3 on 2020-03-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charttype',
            name='subscription_required',
            field=models.BooleanField(default=True),
        ),
    ]