# Generated by Django 2.2.7 on 2019-11-29 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20191128_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='contenty',
            new_name='content',
        ),
    ]