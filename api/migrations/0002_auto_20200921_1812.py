# Generated by Django 3.1.1 on 2020-09-21 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='name',
            field=models.CharField(max_length=18),
        ),
    ]
