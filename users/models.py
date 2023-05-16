from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hackathons(models.Model):
    id = models.AutoField(db_column='Hackathon number', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_date = models.DateField(db_column='End date')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return self.name
    class Meta:
        managed = True
        db_table = 'Hackathons'


class HackathonsRegulations(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    event_date = models.DateField(db_column='Event date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    event_content = models.CharField(db_column='Event content', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    venue = models.CharField(db_column='Venue', max_length=100, blank=True, null=True)  # Field name made lowercase.
    start_time = models.TimeField(db_column='Start time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_time = models.TimeField(db_column='End time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hackathon_number = models.ForeignKey(Hackathons, models.DO_NOTHING, db_column='Hackathon number')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return self.event_content
    class Meta:
        managed = True
        db_table = 'Hackathons Regulations'

class InvitedOrganizations(models.Model):
    letter_number = models.AutoField(db_column='Letter number', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_name = models.CharField(db_column='Organization name', unique=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    manager_surname = models.CharField(db_column='Manager surname', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    manager_name = models.CharField(db_column='Manager name', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    manager_patronymic = models.CharField(db_column='Manager patronymic', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.CharField(db_column='Email', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    letter_subject = models.CharField(db_column='Letter subject', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mailing_day = models.DateField(db_column='Mailing day')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    participant_yes_no_field = models.TextField(db_column='Participant (Yes/No)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    hackathon_number = models.ForeignKey(Hackathons, models.DO_NOTHING, db_column='Hackathon number')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return self.organization_name
    class Meta:
        managed = True
        db_table = 'Invited_organizations'


class Moderators(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=100)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    patronymic = models.CharField(db_column='Patronymic', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100)  # Field name made lowercase.
    login = models.CharField(db_column='Login', unique=True, max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone number', unique=True, max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hackathon_number = models.ForeignKey(Hackathons, models.DO_NOTHING, db_column='Hackathon number')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return self.name
    class Meta:
        managed = True
        db_table = 'Moderators'


class Participants(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    patronymic = models.CharField(db_column='Patronymic', max_length=100, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.DateField(db_column='Birth date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    place_of_study = models.CharField(db_column='Place of study', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    place_of_work = models.CharField(db_column='Place of work', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.CharField(db_column='Email', unique=True, max_length=100)  # Field name made lowercase.
    login = models.CharField(db_column='Login', unique=True, max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.
    team_number = models.ForeignKey('Teams', models.DO_NOTHING, db_column='Team number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hackathon_number = models.ForeignKey(Hackathons, models.DO_NOTHING, db_column='Hackathon number')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Participants'


class ParticipatingOrganizations(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    organization_name = models.CharField(db_column='Organization name', unique=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    manager_surname = models.CharField(db_column='Manager surname', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    manager_name = models.CharField(db_column='Manager name', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    manager_patronymic = models.CharField(db_column='Manager patronymic', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.CharField(db_column='Email', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    link_to_organization_website = models.CharField(db_column='Link to organization website', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    letter_number = models.OneToOneField(InvitedOrganizations, models.DO_NOTHING, db_column='Letter number')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    what_can_provide = models.CharField(db_column='What can provide', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hackathon_number = models.ForeignKey(Hackathons, models.DO_NOTHING, db_column='Hackathon number')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return self.organization_name
    class Meta:
        managed = True
        db_table = 'Participating_organizations'


class ProblemSolution(models.Model):
    evaluation_procedure = models.AutoField(db_column='Evaluation procedure', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stage = models.CharField(db_column='Stage', max_length=100)  # Field name made lowercase.
    team_number = models.ForeignKey('Teams', models.DO_NOTHING, db_column='Team number')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    task_number = models.ForeignKey('Tasks', models.DO_NOTHING, db_column='Task number')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    start_time = models.DateTimeField(db_column='Start time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stage_result = models.CharField(db_column='Stage result', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    expert_review = models.IntegerField(db_column='Expert review')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    resulting_score = models.IntegerField(db_column='Resulting score')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    solution_repository_link_field = models.CharField(db_column='Solution repository (link)', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hackathon_number = models.ForeignKey(Hackathons, models.DO_NOTHING, db_column='Hackathon number')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Problem_solution'


class RepresentativesOrganizations(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    organization_number = models.ForeignKey(ParticipatingOrganizations, models.DO_NOTHING, db_column='number', null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    post = models.CharField(db_column='Post', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status_at_the_event = models.CharField(db_column='Status at the event', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Representatives_organizations'


class Tasks(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=100)  # Field name made lowercase.
    participating_organization_number = models.ForeignKey(ParticipatingOrganizations, models.DO_NOTHING, db_column='Participating organization number')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    link_to_the_task_text = models.CharField(db_column='Link to the task text', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hackathon_number = models.ForeignKey(Hackathons, models.DO_NOTHING, db_column='Hackathon number')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return self.category
    class Meta:
        managed = True
        db_table = 'Tasks'


class Teams(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Team name', unique=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number = models.ForeignKey(Tasks, models.DO_NOTHING, db_column='Task number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    moderator_number = models.ForeignKey(Moderators, models.DO_NOTHING, db_column='Moderator number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hackathon_number = models.ForeignKey(Hackathons, models.DO_NOTHING, db_column='Hackathon number')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return self.name
    class Meta:
        managed = True
        db_table = 'Teams'

class MemberTeam(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.user.username
    def team_members(self, team):
        return MemberTeam.objects.filter(team=team)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    middle_name = models.CharField(max_length=30, null=True)
    job = models.CharField(max_length=100, null=True)
    birth_date = models.DateField()

    def __str__(self):
        return self.user.username