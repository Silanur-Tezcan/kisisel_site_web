# Generated by Django 5.1.6 on 2025-04-19 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_remove_sertifika_kategori_sertifika_kategoriler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sertifika',
            name='kategoriler',
        ),
        migrations.AddField(
            model_name='sertifika',
            name='kategori',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.category'),
        ),
    ]
