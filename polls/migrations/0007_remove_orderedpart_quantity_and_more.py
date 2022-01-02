# Generated by Django 4.0 on 2022-01-02 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alter_shippment_description_alter_shippment_due_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedpart',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderedpart',
            name='quantity_expected',
            field=models.IntegerField(default=20, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderedpart',
            name='quantity_received',
            field=models.IntegerField(default=10, max_length=16),
            preserve_default=False,
        ),
    ]
