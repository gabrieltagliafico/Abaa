# Generated by Django 3.2.7 on 2021-09-14 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0010_auto_20210914_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='detalle',
            field=models.CharField(max_length=254, verbose_name='detalle'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='nombre'),
        ),
    ]
