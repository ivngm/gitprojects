# Generated by Django 3.1.2 on 2020-10-17 18:10

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_menu_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='page',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='page',
            field=modelcluster.fields.ParentalKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='menus.menu'),
            preserve_default=False,
        ),
    ]
