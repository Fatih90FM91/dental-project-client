# Generated by Django 3.2.14 on 2023-10-05 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20231005_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('Man', 'Man'), ('Woman', 'Woman'), ('Like Neither', 'Like Neither')], default='Man', max_length=50),
        ),
    ]
