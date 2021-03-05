# Generated by Django 3.0.5 on 2020-08-10 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-id'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
    ]
