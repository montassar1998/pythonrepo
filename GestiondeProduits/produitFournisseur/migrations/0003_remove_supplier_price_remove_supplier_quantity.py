# Generated by Django 4.0.5 on 2022-06-17 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produitFournisseur', '0002_rename_etat_product_state_rename_etat_supplier_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='price',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='quantity',
        ),
    ]