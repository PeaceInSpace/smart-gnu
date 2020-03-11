# Generated by Django 3.0.2 on 2020-03-07 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smart_gnu', '0006_department_node_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='gpio_pin',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='node_mcu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smart_gnu.NodeMCU'),
        ),
        migrations.AddField(
            model_name='nodemcu',
            name='lab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smart_gnu.Lab'),
        ),
        migrations.AlterUniqueTogether(
            name='device',
            unique_together={('device_name', 'node_mcu', 'gpio_pin')},
        ),
        migrations.AlterUniqueTogether(
            name='nodemcu',
            unique_together={('node_mcu_ip', 'lab')},
        ),
        migrations.RemoveField(
            model_name='device',
            name='lab',
        ),
    ]
