# Generated by Django 4.1.2 on 2022-11-05 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_player_tagline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking_player',
            old_name='fee',
            new_name='amount',
        ),
    ]
