# Generated by Django 3.1.7 on 2021-03-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0002_auto_20210302_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileobject',
            name='loc',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
