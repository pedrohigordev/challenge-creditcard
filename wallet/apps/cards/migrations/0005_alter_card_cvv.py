# Generated by Django 4.2.4 on 2023-08-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_alter_card_holder_alter_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cvv',
            field=models.CharField(blank=True, default=1, max_length=4),
            preserve_default=False,
        ),
    ]
