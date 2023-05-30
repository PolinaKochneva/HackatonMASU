# Generated by Django 4.1.7 on 2023-05-15 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepresentativesOrganizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(blank=True, db_column='Post', max_length=100, null=True)),
                ('status_at_the_event', models.CharField(blank=True, db_column='Status at the event', max_length=100, null=True)),
                ('organization_number', models.ForeignKey(db_column='number', on_delete=django.db.models.deletion.DO_NOTHING, to='users.participatingorganizations')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Representatives_organizations',
                'managed': True,
            },
        ),
    ]