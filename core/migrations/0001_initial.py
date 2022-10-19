# Generated by Django 4.0 on 2022-10-17 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('fee', models.IntegerField()),
                ('target_score', models.IntegerField()),
                ('chase_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Match_venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Match_player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_due_amount', models.IntegerField()),
                ('payment_amount', models.IntegerField()),
                ('player_batting_score', models.IntegerField()),
                ('player_bowling_score', models.IntegerField()),
                ('player_over', models.IntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.player')),
                ('player_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.team')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.match_venue'),
        ),
    ]
