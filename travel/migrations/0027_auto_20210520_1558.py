# Generated by Django 3.0.8 on 2021-05-20 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0026_auto_20210512_1824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='tag',
            new_name='tags',
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(blank=True, help_text='tags', max_length=200, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Tour')),
            ],
        ),
    ]
