# Generated by Django 4.1.2 on 2022-11-05 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_fee_booking_player_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_player',
            name='date',
            field=models.DateField(default='2022-05-05'),
            preserve_default=False,
        ),
    ]
