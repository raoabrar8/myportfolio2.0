# Generated by Django 5.1 on 2024-08-23 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_contactsmodel_profilemodel_showcontactsmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmodel',
            name='name',
            field=models.CharField(default=None, max_length=40),
        ),
    ]
