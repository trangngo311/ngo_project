# Generated by Django 2.2.2 on 2019-06-13 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0003_auto_20190613_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=75, unique=True),
        ),
    ]
