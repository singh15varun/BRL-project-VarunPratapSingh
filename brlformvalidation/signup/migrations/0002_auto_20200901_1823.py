# Generated by Django 3.0.7 on 2020-09-01 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='branch',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='information',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='information',
            name='roll_no',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='name',
            field=models.CharField(default='', max_length=35),
        ),
    ]