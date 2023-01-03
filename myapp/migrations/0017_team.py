# Generated by Django 4.1.4 on 2023-01-03 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_contact_email_alter_contact_full_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='portfolio_pics')),
                ('position', models.CharField(max_length=50)),
            ],
        ),
    ]