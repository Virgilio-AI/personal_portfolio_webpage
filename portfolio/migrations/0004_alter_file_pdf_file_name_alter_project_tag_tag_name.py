# Generated by Django 4.0.3 on 2022-09-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_file_pdf_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_pdf',
            name='file_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='project_tag',
            name='tag_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]