# Generated by Django 4.0.4 on 2022-06-03 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_isemailvalid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='isEmailValid',
            field=models.BooleanField(default=False),
        ),
    ]
