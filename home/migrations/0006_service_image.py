# Generated by Django 3.2.4 on 2021-09-06 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210905_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
