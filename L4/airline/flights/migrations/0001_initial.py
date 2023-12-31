# Generated by Django 4.2.3 on 2023-07-29 12:24

# Created by command python3 manage.py makemigrations
# Step 1 Here are some changes I would like to make to the database
# Step 2 is taking the instructions and applying them

#Instructions to Django on how to create the database
# python3 manage.py migrate creates the database table

# Commands to create
# python3 manage.py shell
# from flights.models import Flight
# f = Flight(origin="New York", destination="London", duration=415)
# f.save()

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=64)),
                ('destination', models.CharField(max_length=64)),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
