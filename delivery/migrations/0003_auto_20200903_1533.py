# Generated by Django 3.0.7 on 2020-09-03 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('milkdairy', '0020_auto_20200903_1501'),
        ('delivery', '0002_auto_20200902_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderrelaton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_boy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.Deliveryboy')),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milkdairy.Ordersummery')),
            ],
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]