# Generated by Django 3.0.8 on 2021-06-11 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0034_auto_20210520_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.TextField(help_text='What do you thing about this game!', max_length=100),
        ),
    ]
