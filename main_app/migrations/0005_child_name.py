# Generated by Django 2.1.2 on 2018-10-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20181016_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
