# Generated by Django 4.0.5 on 2022-06-21 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0004_categoria_receita_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]