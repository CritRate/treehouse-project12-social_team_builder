# Generated by Django 2.2.3 on 2019-07-27 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190727_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='past_projects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Project'),
        ),
    ]
