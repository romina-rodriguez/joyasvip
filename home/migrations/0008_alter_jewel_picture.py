# Generated by Django 4.0 on 2021-12-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_jewel_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewel',
            name='picture',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
