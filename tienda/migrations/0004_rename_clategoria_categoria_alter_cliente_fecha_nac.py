# Generated by Django 4.0.4 on 2022-04-12 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_cliente'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clategoria',
            new_name='Categoria',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nac',
            field=models.DateField(verbose_name='fecha de nacimiento'),
        ),
    ]
