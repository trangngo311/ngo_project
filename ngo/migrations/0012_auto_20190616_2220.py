# Generated by Django 2.2.2 on 2019-06-17 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0011_auto_20190616_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='/static/ngo/images/no_image_available.jpg', upload_to='media/%Y/%m/%d'),
        ),
    ]
