# Generated by Django 3.2.8 on 2021-11-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0002_products_pconcentration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='pDescription',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
