from django.urls import path
from .views import prise_rdv

urlpatterns = [
    path('', prise_rdv, name="rdv-index")
]