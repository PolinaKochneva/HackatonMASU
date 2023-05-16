from django.contrib import admin
from .models import Tasks, Teams, Moderators, ParticipatingOrganizations, InvitedOrganizations, MemberTeam, Profile, Hackathons, HackathonsRegulations, RepresentativesOrganizations

# Register your models here.
admin.site.register(Tasks)
admin.site.register(Teams)
admin.site.register(Moderators)
admin.site.register(ParticipatingOrganizations)
admin.site.register(InvitedOrganizations)
admin.site.register(MemberTeam)
admin.site.register(Profile)
admin.site.register(Hackathons)
admin.site.register(HackathonsRegulations)
admin.site.register(RepresentativesOrganizations)