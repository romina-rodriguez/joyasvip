# Generated by Django 4.0 on 2021-12-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_jewel_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewel',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
