# Generated by Django 2.2 on 2020-09-10 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200908_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
