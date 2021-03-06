# Generated by Django 2.2 on 2020-11-22 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('driver_image', models.ImageField(upload_to='uploads/driver/')),
                ('password', models.CharField(max_length=500)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('address1', models.CharField(default='', max_length=200)),
                ('apt', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('zipcode', models.CharField(default='', max_length=100)),
                ('phone_number', models.CharField(default='', max_length=100)),
                ('vehical_type', models.CharField(max_length=100)),
                ('social_security', models.CharField(default='', max_length=200)),
                ('license_number', models.CharField(default='', max_length=200)),
                ('islicense', models.CharField(default='', max_length=100)),
                ('account_number', models.CharField(default='', max_length=100)),
                ('routing_number', models.CharField(default='', max_length=100)),
                ('convicted_of_any_felonies', models.IntegerField(default=0)),
                ('concede_to_a_background_check', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
    ]
