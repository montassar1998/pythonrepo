# Generated by Django 4.0.5 on 2022-06-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ref',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
    ]