# Generated by Django 3.1.4 on 2021-01-20 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210115_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLoyaltyStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earned_loyalty_points', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('donated_loyalty_points', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('total_loyalty_points', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('going_to_event', models.BooleanField(default=False)),
                ('user_profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_profile', to='profiles.userprofile')),
            ],
        ),
    ]