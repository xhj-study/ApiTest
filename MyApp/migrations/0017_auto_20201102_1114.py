# Generated by Django 2.2 on 2020-11-02 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0016_db_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_step',
            name='index',
            field=models.IntegerField(null=True),
        ),
    ]