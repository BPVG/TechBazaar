# Generated by Django 4.1.5 on 2023-02-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listinguser',
            field=models.CharField(max_length=2000),
        ),
    ]
