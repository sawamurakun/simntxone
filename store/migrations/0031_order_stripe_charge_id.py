# Generated by Django 2.2.3 on 2020-12-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_auto_20201219_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_charge_id',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]