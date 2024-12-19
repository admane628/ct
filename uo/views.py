from django.shortcuts import render, get_object_or_404, redirect
from .models import Formation, UE

# Create your views here.
def about(request):
    return render(request, "about.html")

def formation(request, id):
    fm = get_object_or_404(Formation, id=id)
    ues = UE.objects.filter(formations=fm)
    return render(request, "formation.html", {"formation": fm, "ues":ues})

def ue_view(request, id):
    u = get_object_or_404(UE, id=id)
    return render(request, "ue_view.html", {"ue":u})

def formations(request):
    fm = Formation.objects.all()
    return render(request, "formations.html", {"fm":fm})

def ues(request):
    ues = UE.objects.all()
    return render(request, "ues.html", {"ues":ues})
