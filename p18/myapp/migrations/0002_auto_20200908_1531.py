# Generated by Django 2.2 on 2020-09-08 10:01

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='first_name',
            field=models.CharField(max_length=50, validators=[myapp.models.validate_name]),
        ),
    ]