# Generated by Django 2.0.6 on 2018-11-15 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20181115_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='client',
            field=models.CharField(max_length=200, verbose_name='browser'),
        ),
    ]
