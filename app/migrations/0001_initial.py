# Generated by Django 3.2.3 on 2024-04-03 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kingdom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kingdom_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kingdom')),
            ],
        ),
        migrations.CreateModel(
            name='Subordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('age', models.PositiveSmallIntegerField()),
                ('email', models.CharField(max_length=128)),
                ('kingdom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kingdom')),
            ],
        ),
        migrations.CreateModel(
            name='King',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('kingdom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kingdom')),
            ],
        ),
    ]
