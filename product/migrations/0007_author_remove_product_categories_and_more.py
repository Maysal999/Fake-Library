# Generated by Django 5.0.4 on 2024-04-19 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(auto_created=True, max_length=255, verbose_name='слаг')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('lastname', models.CharField(max_length=50, verbose_name='фамилия')),
                ('image', models.ImageField(default=None, upload_to='image/products/', verbose_name='фото')),
                ('bio', models.TextField()),
                ('dateborth', models.DateField()),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='productmedia',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукт'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to='image/products/', verbose_name='фото'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=None, max_length=255, verbose_name='слаг'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=50, verbose_name='названия'),
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product_author', to='product.author'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='ProductMedia',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
