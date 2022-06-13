# Generated by Django 4.0.4 on 2022-06-13 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_erected', models.DateField()),
                ('marker_name', models.CharField(max_length=500)),
                ('marker_text', models.CharField(max_length=500)),
                ('civil_war_site', models.BooleanField()),
                ('notes', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=55)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('condition', models.CharField(max_length=55)),
                ('mapped_location', models.CharField(max_length=55)),
            ],
        ),
    ]