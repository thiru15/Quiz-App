# Generated by Django 2.1 on 2019-06-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct',
            field=models.CharField(max_length=150),
        ),
    ]