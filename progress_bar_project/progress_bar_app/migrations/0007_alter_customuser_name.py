# Generated by Django 5.0.3 on 2024-05-15 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress_bar_app', '0006_customuser_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
