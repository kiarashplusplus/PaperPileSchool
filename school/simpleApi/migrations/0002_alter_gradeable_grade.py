# Generated by Django 3.2.4 on 2021-07-07 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradeable',
            name='grade',
            field=models.TextField(default='ungraded'),
        ),
    ]