# Generated by Django 3.0.7 on 2020-09-02 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hub', '0006_auto_20200830_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hub_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hub_name', models.CharField(max_length=225)),
                ('number', models.IntegerField(default=0)),
                ('address', models.CharField(default='default_address', max_length=400)),
                ('whatsaap_number', models.IntegerField(default=0)),
                ('hub_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
