# Generated by Django 5.0.3 on 2024-03-29 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_hero_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]