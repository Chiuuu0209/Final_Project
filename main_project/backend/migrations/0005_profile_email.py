# Generated by Django 3.0.2 on 2021-05-02 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_mission_group_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
