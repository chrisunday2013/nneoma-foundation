# Generated by Django 4.1.4 on 2022-12-29 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_portfolio_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='full_name',
            new_name='name',
        ),
    ]
