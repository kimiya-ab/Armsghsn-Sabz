# Generated by Django 3.2.7 on 2021-10-31 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChekList', '0005_alter_parameter_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='category',
            field=models.CharField(max_length=50),
        ),
    ]
