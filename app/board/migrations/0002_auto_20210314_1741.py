# Generated by Django 3.1.7 on 2021-03-14 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='board',
            new_name='board_id',
        ),
        migrations.RenameField(
            model_name='habitcardday',
            old_name='habit_card',
            new_name='habit_card_id',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_card',
            new_name='task_card_id',
        ),
        migrations.AlterUniqueTogether(
            name='habitcardday',
            unique_together={('habit_card_id', 'start_week')},
        ),
    ]
