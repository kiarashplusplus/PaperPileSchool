# Generated by Django 3.2.4 on 2021-07-07 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simpleApi', '0005_alter_gradeable_grading_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradeable',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='gradeable',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student', to='simpleApi.student'),
        ),
    ]