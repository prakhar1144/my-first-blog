# Generated by Django 2.2.15 on 2020-09-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200901_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Tag',
            field=models.CharField(choices=[('Ot', 'Other'), ('Sp', 'Space'), ('Te', 'Technology')], default='ot', max_length=2),
        ),
    ]
