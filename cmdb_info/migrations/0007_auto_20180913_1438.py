# Generated by Django 2.0 on 2018-09-13 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb_info', '0006_auto_20180913_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc_info',
            name='old_status',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
    ]
