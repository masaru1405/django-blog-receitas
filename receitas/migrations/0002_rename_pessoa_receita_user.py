# Generated by Django 4.0.5 on 2022-06-23 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='pessoa',
            new_name='user',
        ),
    ]
