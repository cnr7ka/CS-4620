# Generated by Django 2.1 on 2019-02-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill_share', '0003_auto_20190217_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='skill_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_id',
        ),
        migrations.AddField(
            model_name='skill',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
