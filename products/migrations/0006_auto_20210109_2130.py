# Generated by Django 3.1.4 on 2021-01-09 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['pk'], 'verbose_name_plural': 'Categories'},
        ),
    ]
