# Generated by Django 3.2.7 on 2021-09-14 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_alter_servicio_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='detalle',
            field=models.TextField(max_length=254, verbose_name='detalle'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='nombre',
            field=models.TextField(max_length=50, verbose_name='nombre'),
        ),
    ]
