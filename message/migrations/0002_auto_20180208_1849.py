# Generated by Django 2.0.2 on 2018-02-08 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='is_show',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
