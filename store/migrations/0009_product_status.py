# Generated by Django 2.2 on 2020-11-24 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_subcategory_store_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]