# Generated by Django 3.0.2 on 2020-03-01 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200301_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='umuryango',
            name='district',
        ),
    ]
