# Generated by Django 5.1.6 on 2025-04-16 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_remove_projeler_resimler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeler',
            name='aciklama',
            field=models.CharField(max_length=255),
        ),
    ]
