# Generated by Django 3.0.8 on 2020-07-29 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0004_auto_20200729_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='rating',
        ),
        migrations.AddField(
            model_name='entry',
            name='num_pieces',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
