# Generated by Django 3.1.4 on 2021-05-05 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210505_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.PNG', upload_to='media'),
        ),
    ]