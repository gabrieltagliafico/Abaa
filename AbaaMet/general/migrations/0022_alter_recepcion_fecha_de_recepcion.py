# Generated by Django 3.2.7 on 2021-10-15 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0021_auto_20211007_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recepcion',
            name='fecha_de_recepcion',
            field=models.DateField(auto_now_add=True, verbose_name='fecha_de_recepcion'),
        ),
    ]