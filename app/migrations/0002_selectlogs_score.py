# Generated by Django 5.0 on 2023-12-20 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectlogs',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
