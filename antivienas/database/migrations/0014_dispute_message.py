# Generated by Django 5.0.4 on 2024-04-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_remove_dispute_is_guilty_remove_dispute_was_reviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispute',
            name='message',
            field=models.TextField(default='text', max_length=1000),
            preserve_default=False,
        ),
    ]
