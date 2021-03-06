# Generated by Django 2.0 on 2018-09-21 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_internet_ip'),
        ('cmdb_info', '0007_auto_20180913_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nat_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_port', models.IntegerField(unique=True, verbose_name='外网端口')),
                ('intranet_ip', models.GenericIPAddressField(protocol='ipv4', verbose_name='内网ip')),
                ('in_port', models.IntegerField(verbose_name='内网端口')),
                ('domain', models.CharField(blank=True, max_length=100, verbose_name='域名')),
                ('remark', models.CharField(max_length=400, verbose_name='备注/应用')),
                ('user', models.CharField(max_length=100, verbose_name='责任人')),
                ('internet_ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Internet_Ip', verbose_name='外网ip')),
            ],
        ),
    ]
