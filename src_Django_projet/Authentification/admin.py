from django.contrib import admin
from Authentification.models import user
from RDV.models import prendre_rendez_vous
# Register your models here.

admin.site.register(user)
admin.site.register(prendre_rendez_vous)