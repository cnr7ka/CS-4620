# Generated by Django 2.1 on 2019-02-17 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill_share', '0002_auto_20190217_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='id',
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
