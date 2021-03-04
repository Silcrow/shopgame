# Generated by Django 2.2.19 on 2021-03-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandise',
            name='effects',
            field=models.TextField(max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='description',
            field=models.TextField(max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='durability',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
