# Generated by Django 4.2.6 on 2023-10-20 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='pseudo',
        ),
    ]