# Generated by Django 2.2 on 2019-06-07 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
    ]