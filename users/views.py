from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.http import FileResponse
from .forms import LoginForm, RegForm, UserInfoForm, TeamForm, TeamMemberForm, MemberFormset, HackathonForm, HackathonDateForm, AddRepresentativeForm, OrgForm, TaskForm
from .models import Teams, MemberTeam, Profile, Tasks, HackathonsRegulations, Hackathons, Moderators, RepresentativesOrganizations, ParticipatingOrganizations


# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    elif request.user.is_superuser:
        return render(request, "users/admin.html")
    elif RepresentativesOrganizations.objects.filter(user=request.user):
        return render(request, "users/representative_org.html")
    else:
        return render(request, "users/personal.html")

def login_view(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                return  HttpResponseRedirect(reverse('users:profile'))
            else:
                return render(request, 'users/login.html', {
                    'message':'Неправильное имя пользователя или пароль',
                })

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'Вы вышли из системы',
    })

def add_command(request):
    if request.user.is_authenticated:
        teams = Teams.objects.all()
        member_form = MemberFormset()
        return render(request, "users/add_command.html", {
            'teams': teams,
            'formset':member_form
        })
    return render(request, "users/login.html")
def del_command(request):
    if request.user.is_authenticated:
        team = Teams.objects.filter(name=request.user.memberteam.team)
        team.delete()
        return HttpResponseRedirect(reverse("users:command"))
    return render(request, "users/login.html")
def add_member(request):
    if request.user.is_authenticated:
        member_form = TeamMemberForm(request.POST)
        members = member_form.data.getlist('name')
        users = User.objects.filter(username__in=members)
        for user in users:
            team_member = MemberTeam(team=request.user.memberteam.team, user=user)
            team_member.save()
        return HttpResponseRedirect(reverse("users:command"))

    return render(request, "users/login.html")
def del_member(request):
    if request.user.is_authenticated:
        member_form = TeamMemberForm(request.POST)
        members = member_form.data.getlist('name')
        users = User.objects.filter(username__in=members)
        for user in users:
            user.memberteam.delete()
        return HttpResponseRedirect(reverse("users:command"))

    return render(request, "users/login.html")
def command(request):
# Должна быть проверка на существование команды в БД -- ГОТОВО
# Если существует, то запрет на создание -- ГОТОВО
# Если не существует, то проверка есть ли у предлагаемых участников команда -- ГОТОВО
# Если все участники свободны, то создание команды и привязка участников к команде -- ГОТОВО
# Если участник уже в команде, то вывод страницы с инфой о команде и настройками (в html можно настроить)
# Проблема: Нужна таблица с командами, расширить модель User, обработка формы разных размеров -- ГОТОВО
    if request.user.is_authenticated:
        if MemberTeam.objects.filter(user=request.user):
            return render(request, "users/team.html", {'members':request.user.memberteam.team_members(team=request.user.memberteam.team)})
        else:

            if request.method == 'POST':
                team_form = TeamForm(request.POST)
                if team_form.is_valid():
                    team_name = team_form.cleaned_data['team']
                    members = team_form.data.getlist('name')
                    users = User.objects.filter(username__in=members)
                    if (not Teams.objects.filter(name=team_name)) \
                            and (users.count() == int(request.POST['form-TOTAL_FORMS']))\
                            and not all(MemberTeam.objects.filter(user=user) for user in users):
                        team = Teams(name=team_name,
                                     hackathon_number=Hackathons.objects.all()[0],)
                        team.save()
                        for user in users:
                            team_member = MemberTeam(team=team, user=user)
                            team_member.save()
                        team_member = MemberTeam(team=team, user=request.user)
                        team_member.save()
                        return render(request, "users/team.html",
                                      {'members': request.user.memberteam.team_members(team=request.user.memberteam.team)})

                    return render(request, "users/personal.html", {
                        'message':'Команда уже существует, либо пользователей которых вы пытаетесь добавить не существует, либо уже заняты в другой команде',
                    })

                return render(request, "users/personal.html", {

                    'message': 'форма/не/валидна',
                })

            return HttpResponseRedirect(reverse("users:profile"))

    return render(request, "users/login.html")
def register(request):

    if request.method == 'POST':

        form = RegForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            if (not User.objects.filter(username=cd['username'])) and (not User.objects.filter(email=cd['mail'])) :
                User.objects.create_user(username=cd['username'], email=cd['mail'], password=cd['password'])
                user = authenticate(username=cd['username'], password=cd['password'])

                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('users:profile'))

            else:
                return render(request, "users/registration.html", {
                    'message': 'Пользователь существует',
                })
        else:
            return render(request, "users/registration.html", {
                'message':'Неверная форма',
            })
    return render(request, "users/registration.html")


def update_user_info(request):
    if request.method == 'POST' and request.user.is_authenticated:

        form = UserInfoForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            # Обернуть этот блок в try/except
            user = User.objects.get(username=request.user.username)

            if not Profile.objects.filter(user=request.user):
                profile = Profile(user=request.user,
                                  middle_name=cd['middle_name'],
                                  job=cd['job'],
                                  birth_date=cd['birth_date'],)
                user.first_name = cd['first_name']
                user.last_name = cd['last_name']
                if user.email != cd['mail']:
                    user.email = cd['mail']
                profile.save()
                user.save()

            else:
                if user.first_name != cd['first_name']:
                    user.first_name = cd['first_name']

                if user.profile.middle_name != cd['middle_name']:
                    user.profile.middle_name = cd['middle_name']

                if user.last_name != cd['last_name']:
                    user.last_name = cd['last_name']

                if user.email != cd['mail']:
                    user.email = cd['mail']

                if user.profile.job != cd['job']:
                    user.profile.job = cd['job']

                if user.profile.birth_date != cd['birth_date']:
                    user.profile.birth_date = cd['birth_date']

                user.save()
                user.profile.save()

            # Сделать вывод сообщения об изменении данных
            return HttpResponseRedirect(reverse("users:profile"))
        else:
            return render(request, "users/personal.html", {

                'message': 'Неправильно заполненная форма',
            })
    else:
        return HttpResponseRedirect(reverse("users:profile"))

def delete_user(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        User.delete(user)
        logout(request)
        return render(request, 'users/login.html', {
            'message': 'Вы вышли из системы',
        })
    return render(request, "users/login.html")
def schedule(request):
    if request.user.is_authenticated:
        return render(request, 'users/schedule.html',{
            'timetable':HackathonsRegulations.objects.all(),
            'hackathon_date':Hackathons.objects.all()[0],
        })
    return render(request, "users/login.html")
def task(request):
    if request.user.is_authenticated:
        if MemberTeam.objects.filter(user=request.user):
            if request.user.memberteam.team.task_id:
                return render(request, 'users/user_task.html', {
                    'task':Tasks.objects.get(id=request.user.memberteam.team.task_id.id)
                })
            else:
                return render(request, 'users/tasks.html', {
            'tasks':Tasks.objects.all()
        })

        else:
            return render(request, 'users/tasks.html', {
                'tasks': Tasks.objects.all()
            })
    return render(request, "users/login.html")

def new_task(request):
    if request.user.is_authenticated:
        if MemberTeam.objects.filter(user=request.user):
            team = request.user.memberteam.team
            task = Tasks.objects.get(id=request.POST['task'])
            team.task_id = task
            team.save()
            return HttpResponseRedirect(reverse('users:task'))
        return render(request, "users/personal.html", {
            'message': 'Соберите команду, чтобы выбрать задачу',
        })
    return render(request, "users/login.html")

def change_task(request):
    if request.user.is_authenticated:
        team = request.user.memberteam.team
        team.task_id = None
        team.save()
        return HttpResponseRedirect(reverse('users:task'))
    return render(request, "users/login.html")
#Admin
def new_hackathon(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if not Hackathons.objects.all() and request.method == 'POST':
            form = HackathonForm(request.POST)

            if form.is_valid():
                cd = form.cleaned_data

                hackathon = Hackathons(name=cd['name'],
                                        start_date=cd['start_date'],
                                        end_date=cd['end_date'], )

                hackathon.save()
        return render(request, "users/admin.html", {
            'message': 'Не может быть более двух Хакатонов одновременно',
        })
    return render(request, "users/login.html")

def update_date_hackathon(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = HackathonDateForm(request.POST)

            if form.is_valid():
                cd = form.cleaned_data
                hackathon = Hackathons.objects.all()[0]
                hackathon.start_date = cd['start_date']
                hackathon.end_date = cd['end_date']

                hackathon.save()
            return HttpResponseRedirect(reverse('hackaton:index'))
        return render(request, "users/admin.html", {
            'message': 'Произошла ошибка',
        })
    return render(request, "users/login.html")


#ДОДЕЛАТЬ!
def add_representative(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = AddRepresentativeForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = User.objects.get(username=cd['name'])
                if not RepresentativesOrganizations.objects.filter(user=user):


                    representative = RepresentativesOrganizations(user=user)

                    representative.save()
                    return HttpResponseRedirect(reverse("users:profile"))

                return render(request, "users/representative_org.html", {
                    'message': 'Пользователь уже является представителем некой организации',
                })
            return render(request, "users/representative_org.html", {
                'message': 'Форма не валидна',
            })
        return render(request, "users/representative_org.html", {
            'message': 'Форма не верна',
        })
    return render(request, "users/login.html")

def add_org(request):
    if request.user.is_authenticated and RepresentativesOrganizations.objects.filter(user=request.user):
        if request.method == 'POST':
            form = OrgForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data

                if not ParticipatingOrganizations.objects.filter(organization_name=cd['org_name']):


                    org = ParticipatingOrganizations(organization_name=cd['org_name'],
                                                     manager=RepresentativesOrganizations.objects.get(user=request.user),
                                                     email=cd['org_name'],
                                                     link_to_organization_website=cd['link_to_organization_website'],
                                                     what_can_provide=cd['what_can_provide'],
                                                     hackathon_number=Hackathons.objects.all()[0])

                    org.save()
                    return HttpResponseRedirect(reverse("users:profile"))

                return render(request, "users/representative_org.html", {
                    'message': 'Организация уже зарегистрирована',
                })
            return render(request, "users/representative_org.html", {
                'message': 'Форма не валидна',
            })
        return render(request, "users/representative_org.html", {
            'message': 'Форма не верна',
        })
    return render(request, "users/login.html")

def update_org(request):
    if request.user.is_authenticated and RepresentativesOrganizations.objects.filter(user=request.user):
        if request.method == 'POST':
            form = OrgForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data

                if ParticipatingOrganizations.objects.filter(organization_name=cd['org_name']):

                    org = ParticipatingOrganizations.objects.get(manager=RepresentativesOrganizations.objects.get(user=request.user))

                    if org.organization_name != cd['org_name']:
                        org.organization_name = cd['org_name']

                    if org.email != cd['email']:
                        org.email = cd['email']

                    if org.link_to_organization_website != cd['link_to_organization_website']:
                        org.link_to_organization_website = cd['link_to_organization_website']

                    if org.what_can_provide != cd['what_can_provide']:
                        org.what_can_provide = cd['what_can_provide']

                    org.save()
                    return HttpResponseRedirect(reverse("users:profile"))

                return render(request, "users/representative_org.html", {
                    'message': 'Организация не зарегистрирована',
                })
            return render(request, "users/representative_org.html", {
                'message': 'Форма не валидна',
            })
        return render(request, "users/representative_org.html", {
            'message': 'Форма не верна',
        })
    return render(request, "users/login.html")

def add_task(request):
    if request.user.is_authenticated and RepresentativesOrganizations.objects.filter(user=request.user):
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data

                if not Tasks.objects.filter(purpose=cd['purpose']) and request.user.representativesorganizations.org:


                    task = Tasks(participating_organization_number=ParticipatingOrganizations.objects.get(manager=request.user.representativesorganizations),
                                 purpose=cd['purpose'],
                                 description=cd['description'],
                                 input_data=cd['input_data'],
                                 hackathon_number=Hackathons.objects.all()[0])

                    task.save()
                    return HttpResponseRedirect(reverse("users:profile"))

                return render(request, "users/representative_org.html", {
                    'message': 'Задача уже создана либо вы не зарегистрировали организацию',
                })
            return render(request, "users/representative_org.html", {
                'message': 'Форма не валидна',
            })
        return render(request, "users/representative_org.html", {
            'message': 'Форма не верна',
        })
    return render(request, "users/login.html")