# Generated by Django 3.1 on 2020-09-02 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('URLHandler', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturl',
            name='qr_code',
        ),
    ]
