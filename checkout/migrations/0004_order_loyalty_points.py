# Generated by Django 3.1.4 on 2021-01-16 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='loyalty_points',
            field=models.IntegerField(default=0),
        ),
    ]