# Generated by Django 3.0.3 on 2020-03-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astore', '0006_auto_20200303_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDImg',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='product image'),
        ),
    ]