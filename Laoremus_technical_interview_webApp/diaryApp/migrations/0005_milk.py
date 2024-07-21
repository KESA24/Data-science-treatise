# Generated by Django 3.2 on 2021-12-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaryApp', '0004_delete_milk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('amount', models.IntegerField()),
                ('taste', models.CharField(choices=[('1', 'HIGHQUALITY'), ('2', 'AVERAGE'), ('3', 'BELOWAVERAGE')], max_length=1)),
                ('smell', models.CharField(choices=[('1', 'HIGHQUALITY'), ('2', 'AVERAGE'), ('3', 'BELOWAVERAGE')], max_length=1)),
                ('delivery', models.CharField(choices=[('1', 'HIGHQUALITY'), ('2', 'AVERAGE'), ('3', 'BELOWAVERAGE')], max_length=1)),
                ('adulteration', models.CharField(choices=[('1', 'NONE'), ('2', 'LOW'), ('3', 'HIGH')], max_length=1)),
            ],
        ),
    ]