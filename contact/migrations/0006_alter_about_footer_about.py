# Generated by Django 4.1.7 on 2023-03-12 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_about_footer_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='footer_about',
            field=models.TextField(max_length=200),
        ),
    ]
