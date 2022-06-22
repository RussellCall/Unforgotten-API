# Generated by Django 4.0.4 on 2022-06-13 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0002_alter_marker_year_erected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=15),
        ),
        migrations.AlterField(
            model_name='marker',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=15),
        ),
    ]
