# Generated by Django 5.1.6 on 2025-04-19 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_remove_sertifika_dosya'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sertifika',
            name='kategori',
        ),
        migrations.AddField(
            model_name='sertifika',
            name='kategoriler',
            field=models.ManyToManyField(blank=True, to='pages.category'),
        ),
    ]
