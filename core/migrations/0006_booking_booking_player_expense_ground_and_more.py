# Generated by Django 4.1.2 on 2022-11-03 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_fund_amount_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking_Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField()),
                ('fee_paid', models.BooleanField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.booking')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.player')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='match',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='match_player',
            name='match',
        ),
        migrations.RemoveField(
            model_name='match_player',
            name='player',
        ),
        migrations.RemoveField(
            model_name='match_player',
            name='player_team',
        ),
        migrations.DeleteModel(
            name='Fund',
        ),
        migrations.DeleteModel(
            name='Match',
        ),
        migrations.DeleteModel(
            name='Match_player',
        ),
        migrations.DeleteModel(
            name='Match_venue',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.AddField(
            model_name='booking',
            name='ground',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ground'),
        ),
    ]