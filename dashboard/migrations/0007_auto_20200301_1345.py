# Generated by Django 3.0.2 on 2020-03-01 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_umuryango_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='umuryango',
            name='district',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='dashboard.District'),
        ),
    ]