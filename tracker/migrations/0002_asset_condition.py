# Generated by Django 4.2.1 on 2023-05-10 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='condition',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
