# Generated by Django 4.1.4 on 2022-12-29 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='portfolio_pics'),
        ),
    ]
