# Generated by Django 2.2.2 on 2019-06-16 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0005_auto_20190616_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
