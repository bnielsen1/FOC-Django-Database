# Generated by Django 4.0 on 2022-01-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_alter_po_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedpart',
            name='quantity_received',
            field=models.IntegerField(default=0),
        ),
    ]
