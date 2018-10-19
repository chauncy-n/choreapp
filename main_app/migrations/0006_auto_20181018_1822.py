# Generated by Django 2.1.2 on 2018-10-18 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_child_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='child',
            name='chores',
            field=models.ManyToManyField(to='main_app.Chore', verbose_name='Add a chore'),
        ),
    ]