# Generated by Django 5.1 on 2024-09-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_book_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-date_added']},
        ),
        migrations.AlterField(
            model_name='book',
            name='body',
            field=models.TextField(blank=True, default='Book', null=True),
        ),
    ]
