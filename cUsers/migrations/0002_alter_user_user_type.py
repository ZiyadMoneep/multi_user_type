# Generated by Django 3.2.5 on 2022-01-24 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cUsers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Employer'), (2, 'Employee'), (3, 'secretary'), (4, 'supervisor')]),
        ),
    ]
