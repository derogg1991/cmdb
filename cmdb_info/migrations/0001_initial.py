# Generated by Django 2.0 on 2018-09-11 07:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Network_Device_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=200, verbose_name='序列号')),
                ('ecar_no', models.CharField(blank=True, max_length=200, verbose_name='资产编号')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, protocol='ipv4', unique=True, verbose_name='管理IP')),
                ('user', models.CharField(max_length=200, verbose_name='责任人')),
                ('create_date', models.DateField(verbose_name='购买日期')),
                ('modi_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='变动时间')),
                ('status', models.CharField(choices=[('闲置', '闲置'), ('正常使用', '正常使用'), ('维修', '维修'), ('报废', '报废')], default='正常使用', max_length=100, verbose_name='设备状态')),
                ('port', models.IntegerField(verbose_name='端口数')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Location', verbose_name='存放/使用地点')),
                ('producter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Producter', verbose_name='品牌型号')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Device_type', verbose_name='设备类型')),
            ],
            options={
                'verbose_name_plural': '网络设备详情',
            },
        ),
        migrations.CreateModel(
            name='Pc_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=200, verbose_name='SN序列号')),
                ('ecar_no', models.CharField(blank=True, max_length=100, unique=True, verbose_name='资产编号')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, protocol='ipv4', unique=True, verbose_name='IP')),
                ('user', models.CharField(blank=True, max_length=100, verbose_name='责任人')),
                ('creat_date', models.DateField(verbose_name='购买日期')),
                ('modi_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='变动时间')),
                ('status', models.CharField(choices=[('闲置', '闲置'), ('正常使用', '正常使用'), ('维修', '维修'), ('报废', '报废')], default='正常使用', max_length=100, verbose_name='设备状态')),
                ('cpu', models.CharField(max_length=200, verbose_name='CPU')),
                ('mem', models.IntegerField(verbose_name='内存(G)')),
                ('disk', models.IntegerField(verbose_name='硬盘(G)')),
                ('remark', models.TextField(default='维修更改记录:', verbose_name='备注')),
                ('localtion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Location', verbose_name='存放/使用地点')),
                ('producter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Producter', verbose_name='品牌型号')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Device_type', verbose_name='设备类型')),
            ],
            options={
                'verbose_name': '设备资产信息',
                'verbose_name_plural': '电脑资产信息',
            },
        ),
        migrations.CreateModel(
            name='Server_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=200, verbose_name='序列号')),
                ('ecar_no', models.CharField(blank=True, max_length=200, unique=True, verbose_name='资产编号')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, protocol='ipv4', unique=True, verbose_name='IP')),
                ('user', models.CharField(max_length=200, verbose_name='责任人')),
                ('create_date', models.DateField(verbose_name='购买日期')),
                ('modi_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='变动时间')),
                ('status', models.CharField(choices=[('闲置', '闲置'), ('正常使用', '正常使用'), ('维修', '维修'), ('报废', '报废')], default='正常使用', max_length=100, verbose_name='设备状态')),
                ('cpu_core', models.IntegerField(verbose_name='CPU核心数/个')),
                ('cpu_thread', models.IntegerField(verbose_name='CPU线程数/个')),
                ('cpu_no', models.IntegerField(default=1, verbose_name='CPU个数')),
                ('mem', models.IntegerField(verbose_name='内存(G)')),
                ('disk', models.IntegerField(verbose_name='磁盘(G)')),
                ('remark', models.TextField(verbose_name='备注')),
                ('localtion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Location', verbose_name='存放/使用地点')),
                ('producter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Producter', verbose_name='品牌型号')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Device_type', verbose_name='设备类型')),
            ],
            options={
                'verbose_name_plural': '线下服务器资产详情',
            },
        ),
    ]
