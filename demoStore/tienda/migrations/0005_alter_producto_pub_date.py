# Generated by Django 4.0.1 on 2022-01-10 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_alter_cliente_doc_ide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='pub_date',
            field=models.DateTimeField(verbose_name='fecha registro'),
        ),
    ]
