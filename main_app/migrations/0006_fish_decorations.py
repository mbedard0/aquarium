# Generated by Django 4.0 on 2021-12-29 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_feeding_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='decorations',
            field=models.ManyToManyField(to='main_app.Decoration'),
        ),
    ]
