# Generated by Django 4.2 on 2023-04-09 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Deadline'),
        ),
    ]