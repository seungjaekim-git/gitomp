# Generated by Django 3.1.4 on 2020-12-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
