# Generated by Django 4.1.7 on 2023-03-12 21:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_rename_our_philosophy1_ourphilosophy_par1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='main_about',
            field=ckeditor.fields.RichTextField(max_length=400),
        ),
    ]
