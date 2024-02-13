# Generated by Django 5.0.2 on 2024-02-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='country',
            field=models.ManyToManyField(to='books.country'),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.IntegerField(),
        ),
    ]