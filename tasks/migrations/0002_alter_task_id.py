# Generated by Django 4.0.2 on 2022-02-26 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]