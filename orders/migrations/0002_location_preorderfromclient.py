# Generated by Django 4.2.1 on 2023-05-27 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, unique=True)),
                ('lattitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PreOrderFromClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('luggage_aprox', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_invited_from_client', models.DecimalField(decimal_places=2, max_digits=13)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('NW', 'New'), ('RW', 'Being Reviewed'), ('AC', 'Accepted'), ('DV', 'Delivered')], default='NW', max_length=2)),
                ('from_adrs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_adr_pre_rder', to='orders.location')),
                ('to_adrs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_ad_pre_order', to='orders.location')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
