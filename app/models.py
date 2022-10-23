from django.db import models

# Create your models here.

class Profile(models.Model):
    kerberos = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    branch = models.CharField(max_length=255)
    hostel = models.CharField(max_length=50, default='N/A')
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.kerberos

def get_image_path(instance, filename):
    return f'{instance.user.kerberos}/{filename}'

class Intro(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    about = models.TextField(max_length=800)
    image_1 = models.ImageField(upload_to=get_image_path)
    image_2 = models.ImageField(upload_to=get_image_path, blank=True)
    image_3 = models.ImageField(upload_to=get_image_path, blank=True)
    public = models.BooleanField(default=True)
    likes = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)

    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.kerberos} - {['Not Approved', 'Approved'][self.approved]}"

class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    intro = models.ForeignKey(Intro, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.kerberos} liked {self.intro.user.kerberos}'