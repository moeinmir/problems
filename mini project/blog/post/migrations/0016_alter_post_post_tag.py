# Generated by Django 3.2.9 on 2021-12-06 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_alter_post_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_tag',
            field=models.ManyToManyField(blank=True, null=True, to='post.Tag'),
        ),
    ]
