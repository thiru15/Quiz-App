# Generated by Django 2.2 on 2019-06-10 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='correct',
            name='answer',
            field=models.CharField(default='green', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='correct',
            name='no_of_correct',
            field=models.IntegerField(),
        ),
    ]