# Generated by Django 3.2.8 on 2021-10-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_audit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditlog',
            name='post_data',
            field=models.JSONField(blank=True, null=True,
                                   verbose_name='Post Data'),
        ),
    ]
