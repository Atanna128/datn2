# Generated by Django 3.0.8 on 2021-06-11 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0035_auto_20210611_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='picture',
        ),
    ]
