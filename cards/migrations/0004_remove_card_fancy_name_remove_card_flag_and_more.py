# Generated by Django 4.2.4 on 2023-08-20 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_alter_card_flag_alter_card_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='fancy_name',
        ),
        migrations.RemoveField(
            model_name='card',
            name='flag',
        ),
        migrations.RemoveField(
            model_name='card',
            name='type',
        ),
        migrations.AddField(
            model_name='card',
            name='brand',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
