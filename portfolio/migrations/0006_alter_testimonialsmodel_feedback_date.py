# Generated by Django 5.1 on 2024-08-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_testimonialsmodel_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonialsmodel',
            name='feedback_date',
            field=models.DateField(blank=True, default='2000-09-27'),
        ),
    ]
