# Generated by Django 4.2.1 on 2023-06-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_git', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
