# Generated by Django 4.0 on 2022-01-02 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_alter_orderedpart_quantity_received'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part',
            old_name='part_name',
            new_name='name',
        ),
    ]