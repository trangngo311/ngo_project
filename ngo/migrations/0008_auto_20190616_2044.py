# Generated by Django 2.2.2 on 2019-06-17 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0007_auto_20190616_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]