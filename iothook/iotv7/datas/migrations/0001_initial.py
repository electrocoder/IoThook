# Generated by Django 4.2.2 on 2023-06-25 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('devices', '0004_alter_device_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_1',
                 models.CharField(help_text='Enter a field name', max_length=30, verbose_name='1. Alan Degeri')),
                ('field_2', models.CharField(blank=True, help_text='Enter a field name', max_length=30,
                                             verbose_name='2. Alan Degeri')),
                ('field_3', models.CharField(blank=True, help_text='Enter a field name', max_length=30,
                                             verbose_name='3. Alan Degeri')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Yayın Tarihi')),
                ('enable', models.BooleanField(default=True, help_text='Aktif/Pasif', verbose_name='Aktif')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
