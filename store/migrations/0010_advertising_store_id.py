# Generated by Django 2.2 on 2020-11-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertising',
            name='store_id',
            field=models.IntegerField(default=1),
        ),
    ]
