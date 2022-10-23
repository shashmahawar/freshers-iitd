from django.shortcuts import render, redirect, HttpResponse
from .models import Intro, Like, Profile
from api.models import forgotToken, KerberosData, registrationToken
from django.contrib.auth.models import User
from django.contrib import auth
from . import utils

# Create your views here.

def home(request):
    return render(request, 'home.html')

def bsw(request):
    return redirect('https://bsw.iitd.ac.in/')

def resources(request):
    return redirect('https://resources.iitdelhi.co/')

def intros(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(kerberos=request.user.username)
        if Intro.objects.filter(user=profile).exists():
            introduced = True
            intro = Intro.objects.get(user=profile)
        else:
            introduced = False
        latest = Intro.objects.filter(approved=True).order_by('-id')[:10]
    else:
        latest = Intro.objects.filter(public=True, approved=True).order_by('-id')[:10]
    hostels = utils.hostels
    return render(request, 'intros.html', locals())

def hostel_intros(request, title):
    if request.user.is_authenticated:
        intros = Intro.objects.filter(user__hostel=title, approved=True).order_by('user__name')
    else:
        intros = Intro.objects.filter(user__hostel=title, public=True, approved=True).order_by('user__name')
    intro_list = []
    for intro in intros:
        intro_list.append(intro)
    return render(request, 'filter_intros.html', locals())

def year_intros(request, title):
    if request.user.is_authenticated:
        intro_list = Intro.objects.filter(user__year=title, approved=True).order_by('user__name')
    else:
        intro_list = Intro.objects.filter(user__year=title, public=True, approved=True).order_by('user__name')
    return render(request, 'filter_intros.html', locals())

def intro(request, username):
    if Profile.objects.filter(kerberos=username).exists():
        profile = Profile.objects.get(kerberos=username)
        if Intro.objects.filter(user=profile).exists():
            intro = Intro.objects.get(user=profile)
            if not intro.approved and request.user.username != profile.kerberos:
                return HttpResponse('<h1>Not Found (404)</h1>')
            likes = Like.objects.filter(intro=intro)
            if request.user.is_authenticated:
                if likes.filter(user=Profile.objects.get(kerberos=request.user.username)).exists():
                    liked = True
            if intro.public:
                return render(request, 'intro.html', locals())
            else:
                if request.user.is_authenticated:
                    return render(request, 'intro.html', locals())
                else:
                    return render(request, 'private_intro.html')
        else:
            return HttpResponse('<h1>Not Found (404)</h1>')
    else:
        return HttpResponse('<h1>Not Found (404)</h1>')

def create_intro(request):
    if request.user.is_authenticated:
        user = Profile.objects.get(kerberos=request.user.username)
        if Intro.objects.filter(user=user).exists():
            return redirect(f'/intro/{request.user.username}/')
        if request.method == 'POST':
            profile = Profile.objects.get(kerberos=request.user.username)
            about = request.POST['about']
            image_1 = request.FILES['image_1']
            m = image_1.name.split('.')
            image_1.name = f'image_1.{m[-1]}'
            if len(request.FILES) > 1:
                image_2 = request.FILES['image_2']
                if not image_2:
                    image_2 = request.FILES['image_3']
                m = image_2.name.split('.')
                image_2.name = f'image_2.{m[-1]}'
            else:
                image_2 = None
            if len(request.FILES) > 2:
                image_3 = request.FILES['image_3']
                m = image_3.name.split('.')
                image_3.name = f'image_3.{m[-1]}'
            else:
                image_3 = None
            public = 'public' in request.POST
            likes = 'likes' in request.POST
            Intro.objects.create(
                user = profile,
                about = about,
                image_1 = image_1,
                image_2 = image_2,
                image_3 = image_3,
                public = public,
                likes = likes
            )
            return redirect(f'/intro/{request.user.username}/')
        profile = Profile.objects.get(kerberos=request.user.username)
        return render(request, 'create.html', locals())
    return redirect('signin')
        

def signin(request):
    return render(request, 'signin.html')

def register(request, token):
    if registrationToken.objects.filter(token=token).exists():
        if request.method == 'POST':
            obj = registrationToken.objects.get(token=token)
            kerberos = obj.kerberos
            obj.delete()
            password = request.POST['password']
            user = User.objects.create_user(username=kerberos, password=password)
            user.save()
            obj = KerberosData.objects.get(kerberos=kerberos)
            Profile.objects.create(
                kerberos = kerberos,
                name = obj.name,
                email = f'{kerberos}@iitd.ac.in',
                branch = utils.get_branch_name(kerberos),
                hostel = obj.hostel,
                year = f'20{kerberos[3:5]}'
            )
            auth.login(request, user)
            return redirect('intros')
        return render(request, 'register.html', {'token': token})
    else:
        return HttpResponse('<h1>Not Found (404)</h1>')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('home')

def reset(request, token):
    if forgotToken.objects.filter(token=token).exists():
        if request.method == 'POST':
            obj = forgotToken.objects.get(token=token)
            kerberos = obj.kerberos
            obj.delete()
            password = request.POST['password']
            user = User.objects.get(username=kerberos)
            user.set_password(password)
            user.save()
            return redirect('signin')
        return render(request, 'reset.html', locals())
    else:
        return HttpResponse('<h1>Not Found (404)</h1>')