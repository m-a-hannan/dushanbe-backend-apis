# Generated by Django 3.1.2 on 2021-02-02 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dushanbe', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bill',
            options={'verbose_name_plural': 'Bills'},
        ),
        migrations.RemoveField(
            model_name='bill',
            name='materials',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='topics',
        ),
        migrations.AddField(
            model_name='bill',
            name='item_serial_no',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='material_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='topic_name',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='unit',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
