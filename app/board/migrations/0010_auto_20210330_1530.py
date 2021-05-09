# Generated by Django 3.1.7 on 2021-03-30 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_auto_20210324_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='use_color',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='habitday',
            name='days',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
