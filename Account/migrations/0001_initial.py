# Generated by Django 4.1.7 on 2023-04-07 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, default=0.0, null=True)),
                ('stock', models.PositiveIntegerField(blank=True, null=True)),
                ('discount_price', models.PositiveIntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Product_Image/')),
                ('Catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.catagory')),
            ],
        ),
    ]
