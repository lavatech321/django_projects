# Generated by Django 3.0.1 on 2020-02-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20200203_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='phone_number',
            field=models.IntegerField(default=True),
        ),
    ]