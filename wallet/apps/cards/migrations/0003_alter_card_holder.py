# Generated by Django 4.2.4 on 2023-08-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_alter_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='holder',
            field=models.CharField(max_length=200),
        ),
    ]
