# Generated by Django 4.1.7 on 2023-06-10 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charttest',
            name='digit',
            field=models.IntegerField(default=0),
        ),
    ]