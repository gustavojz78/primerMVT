# Generated by Django 4.0.3 on 2022-04-07 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('telefono', models.IntegerField()),
                ('cumpleaños', models.CharField(max_length=30)),
            ],
        ),
    ]