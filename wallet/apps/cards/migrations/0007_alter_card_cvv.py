# Generated by Django 4.2.4 on 2023-08-23 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_alter_card_cvv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cvv',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
