# Generated by Django 4.2.2 on 2023-06-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('datas', '0005_alter_data_field_2_alter_data_field_3'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='field_4',
            field=models.CharField(blank=True, help_text='Enter a field name', max_length=30, null=True,
                                   verbose_name='4. Alan Degeri'),
        ),
        migrations.AddField(
            model_name='data',
            name='field_5',
            field=models.CharField(blank=True, help_text='Enter a field name', max_length=30, null=True,
                                   verbose_name='5. Alan Degeri'),
        ),
        migrations.AddField(
            model_name='data',
            name='field_6',
            field=models.CharField(blank=True, help_text='Enter a field name', max_length=30, null=True,
                                   verbose_name='6. Alan Degeri'),
        ),
        migrations.AddField(
            model_name='data',
            name='field_7',
            field=models.CharField(blank=True, help_text='Enter a field name', max_length=30, null=True,
                                   verbose_name='7. Alan Degeri'),
        ),
        migrations.AddField(
            model_name='data',
            name='field_8',
            field=models.CharField(blank=True, help_text='Enter a field name', max_length=30, null=True,
                                   verbose_name='8. Alan Degeri'),
        ),
    ]
