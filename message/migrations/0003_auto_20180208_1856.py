# Generated by Django 2.0.2 on 2018-02-08 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20180208_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message_data',
            new_name='message_date',
        ),
    ]
