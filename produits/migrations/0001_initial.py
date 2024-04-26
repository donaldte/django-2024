# Generated by Django 5.0.4 on 2024-04-25 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('prix', models.FloatField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
