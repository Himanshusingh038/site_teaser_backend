# Generated by Django 4.1.7 on 2023-02-25 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenety',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('icon_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ameneties',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('property_desc', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'db_table': 'properties',
            },
        ),
        migrations.CreateModel(
            name='PropertyAmenetyMappings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('property_id', models.IntegerField(blank=True, null=True)),
                ('amenetiy_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'property_ameneties',
            },
        ),
        migrations.CreateModel(
            name='PropertySurrounding',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('property_id', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('desc', models.CharField(blank=True, max_length=255, null=True)),
                ('distance', models.FloatField(blank=True, null=True)),
                ('property_type', models.CharField(choices=[('map', 'Map'), ('status', 'Status')], max_length=10)),
            ],
            options={
                'db_table': 'property_surroundings',
            },
        ),
    ]
