# Generated by Django 4.1.7 on 2023-03-29 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvitedOrganizations',
            fields=[
                ('letter_number', models.AutoField(db_column='Letter number', primary_key=True, serialize=False)),
                ('organization_name', models.CharField(db_column='Organization name', max_length=100, unique=True)),
                ('manager_surname', models.CharField(db_column='Manager surname', max_length=100)),
                ('manager_name', models.CharField(db_column='Manager name', max_length=100)),
                ('manager_patronymic', models.CharField(blank=True, db_column='Manager patronymic', max_length=100, null=True)),
                ('organization_email', models.CharField(blank=True, db_column='Organization email', max_length=100, null=True, unique=True)),
                ('letter_subject', models.CharField(db_column='Letter subject', max_length=100)),
                ('mailing_day', models.DateField(db_column='Mailing day')),
                ('participant_yes_no_field', models.TextField(blank=True, db_column='Participant (Yes/No)', null=True)),
            ],
            options={
                'db_table': 'Invited_organizations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Moderators',
            fields=[
                ('id', models.AutoField(db_column='Moderator ID', primary_key=True, serialize=False)),
                ('surname', models.CharField(db_column='Moderator surname', max_length=100)),
                ('name', models.CharField(db_column='Moderator name', max_length=100)),
                ('patronymic', models.CharField(blank=True, db_column='Moderator patronymic', max_length=100, null=True)),
                ('email', models.CharField(db_column='Moderator email', max_length=100, unique=True)),
                ('login', models.CharField(db_column='Login', max_length=100, unique=True)),
                ('password', models.CharField(db_column='Password', max_length=100)),
                ('phone_number', models.CharField(blank=True, db_column='Phone number', max_length=15, null=True, unique=True)),
            ],
            options={
                'db_table': 'Moderators',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ParticipatingOrganizations',
            fields=[
                ('participating_organization_number', models.AutoField(db_column='Participating organization number', primary_key=True, serialize=False)),
                ('organization_name', models.CharField(db_column='Organization name', max_length=100, unique=True)),
                ('manager_surname', models.CharField(db_column='Manager surname', max_length=100)),
                ('manager_name', models.CharField(db_column='Manager name', max_length=100)),
                ('manager_patronymic', models.CharField(blank=True, db_column='Manager patronymic', max_length=100, null=True)),
                ('organization_email', models.CharField(blank=True, db_column='Organization email', max_length=100, null=True, unique=True)),
                ('link_to_organization_website', models.CharField(blank=True, db_column='Link to organization website', max_length=100, null=True, unique=True)),
                ('what_can_provide', models.CharField(blank=True, db_column='What can provide', max_length=100, null=True)),
                ('letter_number', models.OneToOneField(db_column='Letter number', on_delete=django.db.models.deletion.DO_NOTHING, to='users.invitedorganizations')),
            ],
            options={
                'db_table': 'Participating_organizations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(db_column='Task number', primary_key=True, serialize=False)),
                ('category', models.CharField(db_column='Category', max_length=100)),
                ('link_to_the_task_text', models.CharField(blank=True, db_column='Link to the task text', max_length=100, null=True)),
                ('participating_organization_number', models.ForeignKey(db_column='Participating organization number', on_delete=django.db.models.deletion.DO_NOTHING, to='users.participatingorganizations')),
            ],
            options={
                'db_table': 'Tasks',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(db_column='Team number', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Team name', max_length=100, unique=True)),
                ('moderator_id', models.ForeignKey(blank=True, db_column='Moderator number', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.moderators')),
                ('task_id', models.ForeignKey(blank=True, db_column='Task number', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.tasks')),
            ],
            options={
                'db_table': 'Teams',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RepresentativesOrganizations',
            fields=[
                ('organization_representative_id', models.AutoField(db_column='Organization Representative ID', primary_key=True, serialize=False)),
                ('organization_representative_surname', models.CharField(db_column='Organization representative surname', max_length=100)),
                ('organization_representative_name', models.CharField(db_column='Organization representative name', max_length=100)),
                ('organization_representative_patronymic', models.CharField(blank=True, db_column='Organization representative patronymic', max_length=100, null=True)),
                ('organization_representative_email', models.CharField(db_column='Organization representative email', max_length=100, unique=True)),
                ('post', models.CharField(blank=True, db_column='Post', max_length=100, null=True)),
                ('status_at_the_event', models.CharField(blank=True, db_column='Status at the event', max_length=100, null=True)),
                ('organization_number', models.ForeignKey(db_column='Organization number', on_delete=django.db.models.deletion.DO_NOTHING, to='users.participatingorganizations')),
            ],
            options={
                'db_table': 'Representatives_organizations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProblemSolution',
            fields=[
                ('evaluation_procedure', models.AutoField(db_column='Evaluation procedure', primary_key=True, serialize=False)),
                ('stage', models.CharField(db_column='Stage', max_length=100)),
                ('start_time', models.DateTimeField(db_column='Start time')),
                ('stage_result', models.CharField(db_column='Stage result', max_length=100)),
                ('expert_review', models.IntegerField(db_column='Expert review')),
                ('resulting_score', models.IntegerField(db_column='Resulting score')),
                ('solution_repository_link_field', models.CharField(db_column='Solution repository (link)', max_length=100)),
                ('task_number', models.ForeignKey(db_column='Task number', on_delete=django.db.models.deletion.DO_NOTHING, to='users.tasks')),
                ('team_number', models.ForeignKey(db_column='Team number', on_delete=django.db.models.deletion.DO_NOTHING, to='users.teams')),
            ],
            options={
                'db_table': 'Problem_solution',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(db_column='Participant ID', primary_key=True, serialize=False)),
                ('surname', models.CharField(blank=True, db_column='Participant surname', max_length=100, null=True)),
                ('name', models.CharField(blank=True, db_column='Participant name', max_length=100, null=True)),
                ('patronymic', models.CharField(blank=True, db_column='Participant patronymic', max_length=100, null=True)),
                ('birth_date', models.DateField(blank=True, db_column='Birth date', null=True)),
                ('place_of_study', models.CharField(blank=True, db_column='Place of study', max_length=100, null=True)),
                ('place_of_work', models.CharField(blank=True, db_column='Place of work', max_length=100, null=True)),
                ('email', models.CharField(db_column='Participant email', max_length=100, unique=True)),
                ('login', models.CharField(db_column='Login', max_length=100, unique=True)),
                ('password', models.CharField(db_column='Password', max_length=100)),
                ('team_number', models.ForeignKey(blank=True, db_column='Team number', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.teams')),
            ],
            options={
                'db_table': 'Participants',
                'managed': True,
            },
        ),
    ]
