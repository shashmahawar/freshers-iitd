from django.contrib import admin
from .models import Intro, Like, Profile

# Register your models here.

class AddSearch(admin.ModelAdmin):
    search_fields = ['kerberos']

admin.site.register(Profile, AddSearch)
admin.site.register(Intro, AddSearch)
admin.site.register(Like)