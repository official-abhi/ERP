# Generated by Django 3.0.7 on 2020-09-03 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0008_delete_deliveryboy'),
        ('milkdairy', '0018_ordersummery'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersummery',
            name='hub',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='hub.Hub_detail'),
        ),
    ]
