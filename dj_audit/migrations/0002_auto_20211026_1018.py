# Generated by Django 3.2.8 on 2021-10-26 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_audit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditlog',
            name='attempt_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='auditlog',
            name='response_body',
            field=models.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='auditlog',
            name='response_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]