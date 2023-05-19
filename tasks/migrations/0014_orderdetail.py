# Generated by Django 4.2 on 2023-05-19 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_order_alter_vehiculo_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.vehiculo')),
            ],
        ),
    ]
