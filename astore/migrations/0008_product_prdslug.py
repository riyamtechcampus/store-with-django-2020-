# Generated by Django 3.0.3 on 2020-03-03 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astore', '0007_product_prdimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDslug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
