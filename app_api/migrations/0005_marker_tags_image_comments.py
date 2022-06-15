# Generated by Django 4.0.4 on 2022-06-14 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_api', '0004_tag_markertag'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='tags',
            field=models.ManyToManyField(through='app_api.MarkerTag', to='app_api.tag'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=100)),
                ('marker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.marker')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('marker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.marker')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]