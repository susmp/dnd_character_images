# Generated by Django 4.1.10 on 2023-08-25 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_rename_image_image_картинка'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='картинка',
            new_name='image',
        ),
    ]
