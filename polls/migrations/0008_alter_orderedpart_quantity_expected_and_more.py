# Generated by Django 4.0 on 2022-01-02 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_remove_orderedpart_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedpart',
            name='quantity_expected',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderedpart',
            name='quantity_received',
            field=models.IntegerField(),
        ),
    ]
