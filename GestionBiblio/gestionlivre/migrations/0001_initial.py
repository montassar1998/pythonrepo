# Generated by Django 4.0.5 on 2022-06-15 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('wikipedia', models.URLField(max_length=2049)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField(blank=True, default=10)),
                ('summary', models.CharField(blank=True, max_length=10000)),
                ('category', models.CharField(blank=True, choices=[('Aventure', 'Aventure'), ('Thriller', 'Thriller'), ('Fantastique', 'Fantastique'), ('Romance', 'Romance'), ('Science-fiction', 'Sciencefiction')], max_length=17)),
                ('stock', models.IntegerField(blank=True, default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionlivre.author')),
            ],
        ),
    ]
