# Generated by Django 3.0.3 on 2020-09-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stockitems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockinfo',
            name='stock_name',
            field=models.CharField(max_length=30),
        ),
    ]
