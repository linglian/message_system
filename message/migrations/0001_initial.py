# Generated by Django 2.0.2 on 2018-02-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user_id', models.CharField(max_length=20)),
                ('to_user_id', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=200)),
                ('message_data', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
