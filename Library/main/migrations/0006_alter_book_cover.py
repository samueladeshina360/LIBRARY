# Generated by Django 5.1 on 2024-09-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_book_body_alter_book_genre_delete_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='images/all.jpg', upload_to='images/'),
        ),
    ]