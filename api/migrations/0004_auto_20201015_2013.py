# Generated by Django 3.1.1 on 2020-10-15 20:13

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200921_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='photo',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='current_price',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]))]),
        ),
        migrations.AlterField(
            model_name='offer',
            name='old_price',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
