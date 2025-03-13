# Generated by Django 5.1.7 on 2025-03-13 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_file', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('players_list', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('character', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('turn', models.BooleanField(default=False)),
                ('hand', models.JSONField(default=list)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='game.game')),
            ],
        ),
    ]
