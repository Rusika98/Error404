# Generated by Django 3.2.9 on 2021-11-16 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KAMULogin', '0006_auto_20211116_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='posts',
            new_name='post',
        ),
        migrations.AlterField(
            model_name='blogposts',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
