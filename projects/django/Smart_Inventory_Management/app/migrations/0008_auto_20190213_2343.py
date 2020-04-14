# Generated by Django 2.1.2 on 2019-02-13 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190213_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLogin',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('Admin', 'admin'), ('Area Manager', 'area manager'), ('Analyzer', 'analyzer'), ('Vendor', 'vendor')], max_length=30)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='logindetails',
            name='address',
        ),
        migrations.RemoveField(
            model_name='logindetails',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='logindetails',
            name='email',
        ),
    ]
