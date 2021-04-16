# Generated by Django 3.1.7 on 2021-04-16 03:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('game_id', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='GameGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('ACTION', 'action'), ('INDIE', 'indie'), ('ADVENTURE', 'adventure'), ('RPG', 'rpg'), ('STRATEGY', 'strategy'), ('SHOOTER', 'shooter'), ('CASUAL', 'casual'), ('SIMULATION', 'simulation'), ('PUZZLE', 'puzzle'), ('ARCADE', 'arcade'), ('PLATFORMER', 'platformer'), ('RACING', 'racing'), ('MASSIVELY_MULTIPLAYER', 'massively_multiplayer'), ('SPORTS', 'sports'), ('FIGHTING', 'fighting'), ('FAMILY', 'family'), ('BOARD_GAMES', 'board_games'), ('EDUCATIONAL', 'educational'), ('CARD', 'card')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('favorite_games', models.CharField(blank=True, max_length=100, null=True)),
                ('registration_date', models.DateField(default=django.utils.timezone.now)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=50)),
                ('rating_score', models.IntegerField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
