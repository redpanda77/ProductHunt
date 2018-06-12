# Generated by Django 2.0.6 on 2018-06-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_score', models.IntegerField(db_index=True, default=0)),
                ('num_vote_up', models.PositiveIntegerField(db_index=True, default=0)),
                ('num_vote_down', models.PositiveIntegerField(db_index=True, default=0)),
                ('name', models.CharField(max_length=255)),
                ('product_id', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('address', models.TextField()),
                ('rating', models.CharField(max_length=255)),
                ('categories', models.TextField()),
                ('coordinates', models.TextField()),
                ('url', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
