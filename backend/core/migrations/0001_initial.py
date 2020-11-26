# Generated by Django 3.1.1 on 2020-11-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('year', models.PositiveSmallIntegerField()),
                ('volume', models.PositiveIntegerField()),
            ],
        ),
    ]
