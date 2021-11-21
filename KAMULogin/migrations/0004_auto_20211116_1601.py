# Generated by Django 3.2.9 on 2021-11-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KAMULogin', '0003_auto_20211116_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('slug', models.SlugField()),
                ('intro', models.TextField()),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.DeleteModel(
            name='posts',
        ),
    ]
