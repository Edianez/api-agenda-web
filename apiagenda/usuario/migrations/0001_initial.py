# Generated by Django 3.2.5 on 2021-07-05 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=8)),
            ],
        ),
    ]