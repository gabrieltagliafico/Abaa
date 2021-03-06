# Generated by Django 3.2.6 on 2021-08-11 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('razon_social', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='razon_social',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='id_cliente',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('id_direccion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='general.direccion')),
                ('id_empresa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='general.empresa')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='general.empresa'),
        ),
    ]
