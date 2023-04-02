from django.contrib import admin
from .models import Tasks, Teams, Moderators, ParticipatingOrganizations, InvitedOrganizations, MemberTeam, Profile

# Register your models here.
admin.site.register(Tasks)
admin.site.register(Teams)
admin.site.register(Moderators)
admin.site.register(ParticipatingOrganizations)
admin.site.register(InvitedOrganizations)
admin.site.register(MemberTeam)
admin.site.register(Profile)