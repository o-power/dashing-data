# Generated by Django 3.0.3 on 2020-03-27 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20200317_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='userchart',
            name='subtitle',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
    ]