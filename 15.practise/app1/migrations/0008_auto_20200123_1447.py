# Generated by Django 3.0.1 on 2020-01-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_test2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test2',
            name='address',
            field=models.TextField(help_text='Enter address', unique=True),
        ),
        migrations.AlterField(
            model_name='test2',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]