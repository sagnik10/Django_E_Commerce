# Generated by Django 3.1.3 on 2021-04-29 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0002_laptops'),
    ]

    operations = [
        migrations.CreateModel(
            name='Furnitures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('desciption', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Mens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('desciption', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Womens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('desciption', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
