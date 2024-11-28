# Generated by Django 5.1.3 on 2024-11-09 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('assigned', 'Assigned'), ('accepted', 'Accepted'), ('declined', 'Declined'), ('picked_up', 'Picked Up'), ('in_transit', 'In Transit'), ('delivered', 'Delivered')], default='assigned', max_length=20)),
                ('pickup_location', models.CharField(max_length=50)),
                ('delivery_location', models.CharField(max_length=50)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.courier')),
            ],
        ),
    ]