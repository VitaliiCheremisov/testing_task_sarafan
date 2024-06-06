# Generated by Django 4.2 on 2024-06-06 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_alter_category_options_alter_subcategory_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название подкатегории')),
                ('slug', models.SlugField(max_length=250, verbose_name='Слаг')),
                ('image_small', models.ImageField(upload_to='media/products/small', verbose_name='Маленькое изображение')),
                ('image_medium', models.ImageField(upload_to='media/products/medium', verbose_name='Среднее изображение')),
                ('image_large', models.ImageField(upload_to='media/products/large', verbose_name='Большое изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.subcategory')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
