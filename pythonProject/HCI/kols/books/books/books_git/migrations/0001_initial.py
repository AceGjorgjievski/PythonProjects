# Generated by Django 4.2.1 on 2023-06-01 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=255)),
                ('year_birth', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
                ('biography', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PublishHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PublicationAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_git.author')),
                ('publishing_house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_git.publishhouse')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_git.author')),
                ('publish_house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_git.publishhouse')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
