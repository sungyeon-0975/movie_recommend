# Generated by Django 3.2.9 on 2021-11-18 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('poster_path', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('runtime', models.IntegerField()),
            ],
        ),
    ]