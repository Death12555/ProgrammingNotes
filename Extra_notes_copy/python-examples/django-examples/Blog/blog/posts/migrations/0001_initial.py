# Generated by Django 5.0 on 2024-01-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Attribute name', max_length=100)),
                ('details', models.CharField(default='Checker value', max_length=100)),
            ],
        ),
    ]
