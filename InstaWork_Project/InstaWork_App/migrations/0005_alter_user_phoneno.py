# Generated by Django 4.0.6 on 2022-07-20 12:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InstaWork_App', '0004_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phoneNo',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]