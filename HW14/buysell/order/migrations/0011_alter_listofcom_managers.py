# Generated by Django 3.2.9 on 2021-11-16 18:41

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_listofcom_status'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='listofcom',
            managers=[
                ('existing_com', django.db.models.manager.Manager()),
            ],
        ),
    ]