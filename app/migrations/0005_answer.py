# Generated by Django 3.2.3 on 2024-04-17 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20240417_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAnswerCorrect', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question')),
                ('subordinate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subordinate')),
            ],
        ),
    ]
