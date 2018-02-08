# Generated by Django 2.0.2 on 2018-02-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('score', models.BigIntegerField()),
                ('is_inline', models.BooleanField()),
                ('register_data', models.DateTimeField(auto_now=True)),
                ('login_data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]