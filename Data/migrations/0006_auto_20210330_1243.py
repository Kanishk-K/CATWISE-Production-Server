# Generated by Django 3.0.7 on 2021-03-30 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0005_auto_20210330_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catwise',
            name='BYW',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='catwise',
            name='CatWISESpec',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='catwise',
            name='CatWISESpecSrc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='catwise',
            name='JMagSrc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='catwise',
            name='OnSpitzerPrg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='catwise',
            name='RaDEC',
            field=models.CharField(max_length=50),
        ),
    ]
