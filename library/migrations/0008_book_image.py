# Generated by Django 5.0.3 on 2024-04-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_book_description_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1, upload_to='book'),
            preserve_default=False,
        ),
    ]
