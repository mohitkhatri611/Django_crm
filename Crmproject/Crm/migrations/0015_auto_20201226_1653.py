# Generated by Django 3.1.3 on 2020-12-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crm', '0014_auto_20201226_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='Enquiry_number',
            field=models.CharField(blank=True, default='ZDTJRTEFCU', max_length=100, unique=True),
        ),
    ]