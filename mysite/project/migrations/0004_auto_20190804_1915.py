# Generated by Django 2.2.3 on 2019-08-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20190804_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positions',
            name='accepted',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
