# Generated by Django 4.2 on 2023-04-09 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_post_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='deadline',
            field=models.DateTimeField(default='', null=True),
        ),
    ]
