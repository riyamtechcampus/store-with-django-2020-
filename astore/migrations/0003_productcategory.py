# Generated by Django 3.0.3 on 2020-03-03 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('astore', '0002_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATname', models.CharField(max_length=50, verbose_name='category name')),
                ('CATdesc', models.TextField(max_length=300, verbose_name='category description')),
                ('CATimage', models.ImageField(upload_to='category/', verbose_name='category image')),
                ('CATparent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='astore.ProductCategory', verbose_name='category parent ')),
            ],
        ),
    ]
