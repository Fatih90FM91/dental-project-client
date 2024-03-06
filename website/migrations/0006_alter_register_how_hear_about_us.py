# Generated by Django 3.2.14 on 2023-10-05 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_register_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='how_hear_about_us',
            field=models.CharField(choices=[('Via Internet', 'Internet'), ('Outdour Ads', 'Ads'), ('Family', 'Via Family'), ('Friend and Neigbors', 'Via Friend'), ('Social Media', 'Social Media'), ('Internet Search Engine via Google', 'Google'), ('Already Patient', 'Already Patient'), ('Other', 'Other')], default='Friend and Neigbors', max_length=50),
        ),
    ]
