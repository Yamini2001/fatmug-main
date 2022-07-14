# Generated by Django 3.1.4 on 2021-07-13 11:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('Title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='auth',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='report',
        ),
        migrations.AddField(
            model_name='articles',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.auth'),
        ),
    ]
