# Generated by Django 3.0.7 on 2020-09-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0008_delete_deliveryboy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub_detail',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
