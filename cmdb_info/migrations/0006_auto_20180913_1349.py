# Generated by Django 2.0 on 2018-09-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb_info', '0005_network_device_info_remark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='network_device_info',
            options={'verbose_name': '网络设备详情', 'verbose_name_plural': '网络设备详情'},
        ),
        migrations.AlterModelOptions(
            name='pc_info',
            options={'verbose_name': '电脑资产详情', 'verbose_name_plural': '电脑资产详情'},
        ),
        migrations.AlterModelOptions(
            name='server_info',
            options={'verbose_name': '线下服务器资产详情', 'verbose_name_plural': '线下服务器资产详情'},
        ),
        migrations.AddField(
            model_name='pc_info',
            name='old_status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='network_device_info',
            name='remark',
            field=models.TextField(blank=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='network_device_info',
            name='status',
            field=models.CharField(choices=[('闲置', '闲置'), ('正常使用', '正常使用'), ('维修', '维修'), ('已报废', '已报废')], default='正常使用', max_length=100, verbose_name='设备状态'),
        ),
        migrations.AlterField(
            model_name='pc_info',
            name='remark',
            field=models.TextField(blank=True, verbose_name='备注/维修更改记录'),
        ),
        migrations.AlterField(
            model_name='pc_info',
            name='status',
            field=models.CharField(choices=[('闲置', '闲置'), ('正常使用', '正常使用'), ('维修', '维修'), ('已报废', '已报废')], default='正常使用', max_length=100, verbose_name='设备状态'),
        ),
        migrations.AlterField(
            model_name='server_info',
            name='remark',
            field=models.TextField(blank=True, verbose_name='备注/涉及项目'),
        ),
        migrations.AlterField(
            model_name='server_info',
            name='status',
            field=models.CharField(choices=[('闲置', '闲置'), ('正常使用', '正常使用'), ('维修', '维修'), ('已报废', '已报废')], default='正常使用', max_length=100, verbose_name='设备状态'),
        ),
    ]