# Generated by Django 4.1.2 on 2022-10-30 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0020_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.album'),
        ),
    ]
