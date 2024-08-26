# Generated by Django 5.1 on 2024-08-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_homemodel_updated_homemodel_whatsapp_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homemodel',
            name='cv_url',
        ),
        migrations.RemoveField(
            model_name='homemodel',
            name='whatsapp_url',
        ),
        migrations.AddField(
            model_name='homemodel',
            name='cv',
            field=models.FileField(blank=True, max_length=200, upload_to=''),
        ),
        migrations.AddField(
            model_name='homemodel',
            name='whatsapp_no',
            field=models.CharField(default='0317 4196972', max_length=200),
        ),
        migrations.AlterField(
            model_name='homemodel',
            name='about_me',
            field=models.TextField(),
        ),
    ]
