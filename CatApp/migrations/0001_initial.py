# Generated by Django 4.2.3 on 2023-07-19 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('breed', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
        ),
    ]
