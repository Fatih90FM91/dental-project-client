# Generated by Django 3.2.21 on 2023-10-07 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_rename_add_member_register_are_you_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.CharField(error_messages={'unique': 'The Email Field you entered already exists.'}, max_length=150, unique=True),
        ),
    ]
