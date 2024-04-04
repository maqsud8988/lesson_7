# Generated by Django 5.0.4 on 2024-04-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_remove_comments_book_bookingbook_comments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingbook',
            name='comments',
        ),
        migrations.AddField(
            model_name='book',
            name='comments',
            field=models.ManyToManyField(to='library.comments'),
        ),
    ]
