# Generated by Django 3.2.7 on 2021-09-27 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0016_auto_20210926_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='id_sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='general.sucursal', verbose_name='sucursal'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre_completo',
            field=models.CharField(max_length=40, null=True, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=12, verbose_name='telefono'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_ad',
            field=models.CharField(max_length=12, null=True, verbose_name='telefono_ad'),
        ),
    ]
