# Generated by Django 2.0.2 on 2018-02-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180208_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='123456', max_length=20),
        ),
    ]
