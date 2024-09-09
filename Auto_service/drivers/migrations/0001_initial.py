# Generated by Django 4.2 on 2024-09-09 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_make', models.CharField(max_length=100)),
                ('vehicle_model', models.CharField(max_length=100)),
                ('vehicle_year', models.PositiveIntegerField()),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
