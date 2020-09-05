# Generated by Django 3.1.1 on 2020-09-03 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='', upload_to='shops/images'),
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='subcategory',
            field=models.CharField(default='', max_length=50),
        ),
    ]
