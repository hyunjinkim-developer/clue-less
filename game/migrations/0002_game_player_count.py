# Generated by Django 5.1.7 on 2025-03-13 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='player_count',
            field=models.IntegerField(default=0),
        ),
    ]
