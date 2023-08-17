# Generated by Django 2.2.9 on 2023-08-17 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fancy_name', models.CharField(blank=True, max_length=100)),
                ('type', models.CharField(choices=[('1', 'credit'), ('2', 'debit')], default=1, max_length=20)),
                ('exp_date', models.DateField()),
                ('holder', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=16)),
                ('cvv', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('flag', models.CharField(choices=[('1', 'Visa'), ('2', 'Mastercard'), ('3', 'Elo'), ('4', 'Dinners Club'), ('5', 'American Express')], default=2, max_length=20)),
            ],
        ),
    ]