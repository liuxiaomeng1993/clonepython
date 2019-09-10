# Generated by Django 2.0.1 on 2019-09-09 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commondity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commondity.Category', verbose_name='父类'),
        ),
        migrations.AlterField(
            model_name='category',
            name='picture_url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='图片路径'),
        ),
    ]
