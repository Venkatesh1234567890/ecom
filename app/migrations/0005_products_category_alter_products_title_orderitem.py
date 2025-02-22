# Generated by Django 5.1.1 on 2024-10-01 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_image_products_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.PositiveIntegerField(default=1)),
                ('odered_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.products')),
            ],
        ),
    ]
