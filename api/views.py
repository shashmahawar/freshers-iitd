from email.mime.text import MIMEText
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import KerberosData, forgotToken, registrationToken
from app.models import Intro, Like, Profile
from django.contrib.auth.models import User
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import auth
from django.conf import settings

# Create your views here.

@api_view(['POST'])
def checkKerberos(request):
    data = request.data
    kerberos = data.get('kerberos').lower()
    if KerberosData.objects.filter(kerberos=kerberos).exists():
        if kerberos[3:5] != '22':
            return Response({'message': 'This drive is currently open for First Year Students only!'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=kerberos).exists():
            return Response({'message': 'Already Registered'}, status=status.HTTP_200_OK)
        else:
            if registrationToken.objects.filter(kerberos=kerberos).exists():
                registrationToken.objects.get(kerberos=kerberos).delete()
            data = '1234567890-ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
            token = ''.join(random.choice(data) for i in range(random.randint(100, 150)))
            if registrationToken.objects.filter(token=token).exists():
                return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
            subject = f'Registration - Freshers@IITD'
            message = f'Hey there! \n\n You have been invited to join Freshers@IITD. Please click on the link below to register yourself. \n {settings.SITE_NAME}/register/{token}/ \n\n If you have not been invited to join Freshers@IITD, please ignore this email. \n\n Regards, \n Shashank Mahawar \n Freshers@IITD'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [f'{kerberos}@iitd.ac.in',]
            try:
                send_mail(subject, message, email_from, recipient_list)
            except:
                return Response({'message': 'Failed to send email'}, status=status.HTTP_400_BAD_REQUEST)
            registrationToken.objects.create(kerberos=kerberos, token=token)
            return Response({'message': 'New Registration'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'Kerberos not found in database'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def login(request):
    data = request.data
    kerberos = data.get('kerberos').lower()
    password = data.get('password')
    if len(password) < 8:
        return Response({'message': 'Password must be atleast 8 characters long'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=kerberos).exists():
        user = auth.authenticate(username=kerberos, password=password)
        if user is not None:
            auth.login(request, user)
            return Response({'message': 'Login Successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid Password'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def manageLike(request):
    data = request.data
    intro = data.get('kerberos').lower()
    if request.user.is_authenticated:
        intro = Intro.objects.get(user__kerberos=intro)
        profile = Profile.objects.get(kerberos=request.user.username)
        if Like.objects.filter(intro=intro, user=profile).exists():
            Like.objects.get(intro=intro, user=profile).delete()
            return Response({'message': 'Like Removed'}, status=status.HTTP_200_OK)
        else:
            Like.objects.create(intro=intro, user=profile)
            return Response({'message': 'Like Added'}, status=status.HTTP_201_CREATED)        
    else:
        return Response({'message': 'User not logged in'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def forgot(request):
    data = request.data
    kerberos = data.get('kerberos').lower()
    if KerberosData.objects.filter(kerberos=kerberos).exists():
        if User.objects.filter(username=kerberos).exists():
            data = '1234567890-ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
            token = ''.join(random.choice(data) for i in range(random.randint(100, 150)))
            if forgotToken.objects.filter(kerberos=kerberos).exists():
                obj = forgotToken.objects.get(kerberos=kerberos)
                obj.token = token
            subject = f'Password Reset - Freshers@IITD'
            message = f'Hey there! \n\n You have requested to reset your password. Please click on the link below to reset your password. \n {settings.SITE_NAME}/reset/{token}/ \n\n If you have not requested to reset your password, please ignore this email. \n\n Regards, \n Shashank Mahawar \n Freshers@IITD'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [f'{kerberos}@iitd.ac.in',]
            try:
                send_mail(subject, message, email_from, recipient_list)
            except:
                return Response({'message': 'Failed to send email'}, status=status.HTTP_400_BAD_REQUEST)
            forgotToken.objects.create(kerberos=kerberos, token=token)
            return Response({'message': 'New Registration'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'User not registered'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'message': 'Kerberos not found in database'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def sitemap(request):
    if request.user.is_superuser:
        res = """<?xml version="1.0" encoding="UTF-8"?>

        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

            <url>
                <loc>https://freshers.iitd.site/</loc>
                <priority>0.8</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/year/2023/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/year/2022/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/year/2021/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/hostel/Aravali/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/hostel/Girnar/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/hostel/Himadri/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/hostel/Jwalamukhi/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/hostel/Kailash/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/hostel/Karakoram/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/hostel/Kumaon/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/hostel/Nilgiri/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/hostel/Sahyadri/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/hostel/Satpura/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/hostel/Shivalik/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/hostel/Udaigiri/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/hostel/Vindhyachal/</loc>
                <priority>0.6</priority>
            </url>

            <url>
                <loc>https://freshers.iitd.site/intro/hostel/Zanskar/</loc>
                <priority>0.6</priority>
            </url>
        """
        intros = Intro.objects.filter(public=True, approved=True)
        for intro in intros:
            res += f"""
            <url>
                <loc>https://freshers.iitd.site/intro/{intro.user.kerberos}/</loc>
                <priority>0.5</priority>
            </url>
            """
        res += """
        </urlset>
        """

        with open(f'{settings.BASE_DIR}/static/sitemap.xml', 'w') as f:
            f.write(res)

        return Response({'message': 'Sitemap Refreshed'}, status=status.HTTP_200_OK)
    return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)