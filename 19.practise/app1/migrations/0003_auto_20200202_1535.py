# Generated by Django 3.0.1 on 2020-02-02 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200202_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='address1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='address2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='zip1',
            field=models.IntegerField(),
        ),
    ]
