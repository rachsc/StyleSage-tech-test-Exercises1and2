# Generated by Django 4.0.1 on 2022-01-26 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_alter_album_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(default=50, on_delete=django.db.models.deletion.CASCADE, to='music.album'),
        ),
    ]
