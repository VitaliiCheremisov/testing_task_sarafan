# Generated by Django 4.2 on 2024-06-06 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Слаг')),
                ('image', models.ImageField(upload_to='media/categories', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название подкатегории')),
                ('slug', models.CharField(max_length=250, verbose_name='Название подкатегории')),
                ('image', models.ImageField(upload_to='media/subcategories')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
        ),
    ]