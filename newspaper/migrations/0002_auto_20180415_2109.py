# Generated by Django 2.1.dev20180415210700 on 2018-04-16 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pubdate']},
        ),
    ]