# Generated by Django 4.0.1 on 2022-02-08 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_sinup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sinup',
            old_name='username',
            new_name='name',
        ),
    ]
