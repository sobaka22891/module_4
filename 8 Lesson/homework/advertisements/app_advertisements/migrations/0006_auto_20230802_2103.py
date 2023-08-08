# Generated by Django 3.2.13 on 2023-08-02 18:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0005_alter_advertisement_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='updated_date',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='created_date',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
    ]
