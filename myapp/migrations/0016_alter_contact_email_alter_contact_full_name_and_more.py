# Generated by Django 4.1.4 on 2023-01-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_testimonial_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='full_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
