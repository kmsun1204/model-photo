# Generated by Django 2.2.4 on 2019-08-06 07:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190806_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_contents',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]