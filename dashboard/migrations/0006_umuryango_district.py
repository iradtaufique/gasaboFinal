# Generated by Django 3.0.2 on 2020-03-01 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_remove_umuryango_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='umuryango',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.District'),
        ),
    ]