# Generated by Django 3.0.5 on 2020-04-15 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post/', verbose_name='Картинка'),
        ),
    ]
