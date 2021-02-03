# Generated by Django 3.1.2 on 2021-02-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dushanbe', '0002_auto_20210202_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='item_serial_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='topic_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='bill',
            unique_together={('bill_name', 'item_serial_no')},
        ),
    ]