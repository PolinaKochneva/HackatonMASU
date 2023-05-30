# Generated by Django 4.1.7 on 2023-05-30 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_participatingorganizations_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='participatingorganizations',
            name='link_to_logo',
            field=models.CharField(blank=True, db_column='Link to logo', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='participatingorganizations',
            name='description',
            field=models.CharField(blank=True, db_column='Description', max_length=1000, null=True),
        ),
    ]
