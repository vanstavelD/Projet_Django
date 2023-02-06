from django.shortcuts import render


def prise_rdv(request):
    return render(request,"rdv.html")