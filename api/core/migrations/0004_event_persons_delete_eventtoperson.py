# Generated by Django 4.0.4 on 2023-04-25 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_type_wallpaper'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='persons',
            field=models.ManyToManyField(to='core.person', verbose_name='Персоны'),
        ),
        migrations.DeleteModel(
            name='EventToPerson',
        ),
    ]
