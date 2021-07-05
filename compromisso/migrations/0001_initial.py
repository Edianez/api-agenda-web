# Generated by Django 3.2.5 on 2021-07-05 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('contato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compromisso',
            fields=[
                ('idcompromisso', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=300)),
                ('local', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('idcontato', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='contato.contato')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='usuario.usuario')),
            ],
        ),
    ]
