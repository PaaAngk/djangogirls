# Generated by Django 2.2.24 on 2021-06-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210625_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сomments',
            name='comment',
            field=models.CharField(max_length=25, null=True),
        ),
    ]