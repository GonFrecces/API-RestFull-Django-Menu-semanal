# Generated by Django 3.0.14 on 2022-06-24 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('Id_dia_semana', models.AutoField(primary_key=True, serialize=False, verbose_name='Id_dia_semana')),
                ('Dia', models.CharField(blank=True, choices=[('Juves', 'Jueves'), ('Sábado', 'Sábado'), ('Lunes', 'Lunes'), ('Viernes', 'Viernes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'), ('Domingo', 'Domingo')], max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('Id_plato', models.AutoField(primary_key=True, serialize=False, verbose_name='Id_plato')),
                ('Nombre', models.CharField(blank=True, max_length=60, null=True)),
                ('Menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plato', to='ACME_APP.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=60, null=True)),
                ('Plato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredientes', to='ACME_APP.Plato')),
            ],
        ),
    ]