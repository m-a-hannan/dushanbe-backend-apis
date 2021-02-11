# Generated by Django 3.1.2 on 2021-02-11 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_name', models.CharField(blank=True, max_length=500, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Bills',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.TextField(blank=True, null=True)),
                ('serial_no', models.PositiveIntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=10, null=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
            options={
                'verbose_name_plural': 'Materials',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(blank=True, max_length=250, null=True)),
                ('bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type_bill', to='dushanbe.bill')),
            ],
            options={
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.CreateModel(
            name='WorkSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateField(blank=True, null=True)),
                ('work_progress', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('active_status', models.BooleanField(blank=True, default=True, null=True)),
                ('bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workubmission_bill', to='dushanbe.bill')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workubmission_created_by', to=settings.AUTH_USER_MODEL)),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workubmission_material', to='dushanbe.material')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workubmission_type', to='dushanbe.type')),
            ],
            options={
                'verbose_name_plural': 'Work Submissions',
            },
        ),
        migrations.AddField(
            model_name='material',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='material_type', to='dushanbe.type'),
        ),
    ]
