# Generated by Django 3.1.1 on 2020-09-25 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200925_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='is_excepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='is_rereleased',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='total_num',
            field=models.IntegerField(default=0),
        ),
    ]
