# Generated by Django 3.1.3 on 2020-12-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crm', '0010_auto_20201224_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='visit_date',
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='Enquiry_number',
            field=models.CharField(blank=True, default='UQOIDYAQCY', max_length=100, unique=True),
        ),
    ]
