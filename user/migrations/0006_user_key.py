# Generated by Django 2.0.2 on 2018-02-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20180208_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='key',
            field=models.CharField(default='0', max_length=50),
        ),
    ]