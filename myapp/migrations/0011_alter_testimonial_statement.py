# Generated by Django 4.1.4 on 2022-12-31 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_portfolio_user_remove_testimonial_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='statement',
            field=models.TextField(max_length=500),
        ),
    ]
