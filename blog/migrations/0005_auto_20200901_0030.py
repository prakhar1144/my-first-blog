# Generated by Django 2.2.15 on 2020-08-31 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200901_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='/static/blog/github.png', null=True, upload_to=''),
        ),
    ]
