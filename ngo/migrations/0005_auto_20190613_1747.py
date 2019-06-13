# Generated by Django 2.2.2 on 2019-06-13 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0004_auto_20190613_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ngo.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('USER', 'User'), ('ADMIN', 'Admin')], default='User', max_length=1),
        ),
    ]