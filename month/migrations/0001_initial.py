# Generated by Django 3.0.7 on 2020-08-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('milkdairy', '0015_auto_20200825_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='January',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('days', models.CharField(max_length=50)),
                ('member_id', models.ManyToManyField(to='milkdairy.Orders')),
            ],
        ),
    ]