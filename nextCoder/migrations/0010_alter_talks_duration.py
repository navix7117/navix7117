# Generated by Django 3.2.6 on 2021-08-24 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nextCoder', '0009_alter_talks_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talks',
            name='duration',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]