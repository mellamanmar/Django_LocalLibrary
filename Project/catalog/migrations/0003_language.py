# Generated by Django 4.2.2 on 2023-06-08 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_author_options_alter_bookinstance_book_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese el lenguaje, ejemplo inglés', max_length=50)),
            ],
        ),
    ]
