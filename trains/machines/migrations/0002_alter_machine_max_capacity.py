# Generated by Django 3.2.8 on 2021-10-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='max_capacity',
            field=models.IntegerField(help_text='Maximum amount of passengers machine can carry'),
        ),
    ]
