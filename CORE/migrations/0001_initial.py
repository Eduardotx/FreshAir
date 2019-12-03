# Generated by Django 2.0.7 on 2018-12-12 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('gender_id', models.IntegerField(primary_key=True, serialize=False)),
                ('gender_desc', models.CharField(max_length=20, verbose_name='gender_desc')),
            ],
        ),
        migrations.CreateModel(
            name='Presupuestos',
            fields=[
                ('name', models.CharField(default='nn', max_length=20, primary_key=True, serialize=False)),
                ('tot_prod', models.IntegerField()),
                ('tot_money', models.IntegerField()),
                ('max_money', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('prod_id', models.IntegerField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(default='name', max_length=20)),
                ('pre_cost', models.IntegerField()),
                ('real_cost', models.IntegerField()),
                ('notes', models.CharField(default='nodesc', max_length=40)),
                ('pres_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CORE.Presupuestos')),
            ],
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('provincia_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='nn', max_length=45, verbose_name='provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Regiones',
            fields=[
                ('region_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='nn', max_length=45, verbose_name='region')),
                ('ordinal', models.CharField(default='I', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Tiendas',
            fields=[
                ('store_id', models.IntegerField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(default='nn', max_length=20)),
                ('office', models.CharField(default='nn', max_length=20)),
                ('adress', models.CharField(default='nn', max_length=20)),
                ('provincia_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CORE.Provincias')),
                ('region_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CORE.Regiones')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('rut', models.CharField(default='nn', max_length=12, primary_key=True, serialize=False)),
                ('username', models.CharField(default='nn', max_length=20)),
                ('passw', models.CharField(default='nn', max_length=20)),
                ('name', models.CharField(default='nn', max_length=20)),
                ('mail', models.CharField(default='nn', max_length=20)),
                ('age', models.IntegerField()),
                ('gender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CORE.Generos')),
            ],
        ),
        migrations.AddField(
            model_name='provincias',
            name='region_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CORE.Regiones'),
        ),
        migrations.AddField(
            model_name='productos',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CORE.Tiendas'),
        ),
        migrations.AddField(
            model_name='presupuestos',
            name='user_rut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CORE.Usuarios'),
        ),
    ]