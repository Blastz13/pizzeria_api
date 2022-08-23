# Generated by Django 4.1 on 2022-08-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
                ('weight', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=1024)),
                ('ingredients', models.ManyToManyField(to='pizza.ingredientpizza')),
            ],
        ),
    ]
