from django.contrib import admin
from .models import KerberosData, forgotToken, registrationToken

# Register your models here.

class AddSearch(admin.ModelAdmin):
    search_fields = ['kerberos']
    ordering = ['kerberos']

admin.site.register(KerberosData, AddSearch)
admin.site.register(registrationToken, AddSearch)
admin.site.register(forgotToken, AddSearch)