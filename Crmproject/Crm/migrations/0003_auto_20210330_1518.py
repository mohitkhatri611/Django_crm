# Generated by Django 3.1.3 on 2021-03-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crm', '0002_auto_20210328_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='Delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='Enquiry_number',
            field=models.CharField(blank=True, default='BHEHULRSHF', max_length=100, unique=True),
        ),
    ]