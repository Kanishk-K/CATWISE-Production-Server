# Generated by Django 3.0.7 on 2021-03-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0004_auto_20210323_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catwise',
            name='FoundInSearch',
            field=models.CharField(max_length=100),
        ),
    ]
