# Generated by Django 4.0.4 on 2022-05-06 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_messaging', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='msg_body',
            new_name='message',
        ),
    ]