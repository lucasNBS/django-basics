# Generated by Django 5.0.3 on 2024-03-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/no-image.jpg', upload_to='images'),
        ),
    ]