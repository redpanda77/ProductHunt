# Generated by Django 2.0.5 on 2018-05-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20180529_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.TextField(),
        ),
    ]
