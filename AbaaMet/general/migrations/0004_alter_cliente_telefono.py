# Generated by Django 3.2.6 on 2021-08-13 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_alter_cliente_id_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=12),
        ),
    ]
