# Generated by Django 4.0.4 on 2022-05-22 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='booked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Appointment', to='management.patient'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='booked_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Appointment', to='management.doctor'),
        ),
    ]
