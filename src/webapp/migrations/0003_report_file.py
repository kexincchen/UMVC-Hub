# Generated by Django 4.2.10 on 2024-02-12 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_date_published_report_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='reports'),
        ),
    ]
