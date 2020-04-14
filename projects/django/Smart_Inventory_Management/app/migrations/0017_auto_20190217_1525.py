# Generated by Django 2.1.2 on 2019-02-17 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20190217_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor_Quotations',
            fields=[
                ('qid', models.IntegerField(primary_key=True, serialize=False)),
                ('tender_id', models.IntegerField()),
                ('vendor_id', models.IntegerField()),
                ('required_product', models.CharField(max_length=20)),
                ('cost_per_item', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supply_date', models.DateField()),
                ('apply_date', models.DateField()),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameModel(
            old_name='Quotations',
            new_name='Admin_Quotations',
        ),
    ]