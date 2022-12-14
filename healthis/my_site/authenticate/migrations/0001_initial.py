# Generated by Django 4.0.3 on 2022-04-29 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('vacine', models.CharField(max_length=100)),
                ('dose', models.IntegerField(max_length=3)),
                ('batch', models.CharField(max_length=100)),
                ('vaccinator', models.CharField(max_length=200)),
            ],
        ),   
    ]
