# Generated by Django 3.2.1 on 2021-05-07 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('binance_bot', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Orders',
        ),
    ]
