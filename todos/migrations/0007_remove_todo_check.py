# Generated by Django 2.2.3 on 2019-07-31 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_auto_20190731_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='check',
        ),
    ]