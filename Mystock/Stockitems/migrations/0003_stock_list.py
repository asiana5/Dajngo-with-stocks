# Generated by Django 3.0.3 on 2020-09-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stockitems', '0002_auto_20200913_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corpName', models.CharField(max_length=200)),
                ('corpCode', models.CharField(max_length=10)),
                ('corpCategory', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]