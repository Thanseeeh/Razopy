# Generated by Django 4.1.8 on 2023-05-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0006_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='main-img.jpg', null=True, upload_to='banner')),
            ],
        ),
    ]
