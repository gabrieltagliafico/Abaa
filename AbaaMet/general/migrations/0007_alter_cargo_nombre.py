# Generated by Django 3.2.7 on 2021-09-13 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_auto_20210912_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='cargo'),
        ),
    ]