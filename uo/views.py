from django.shortcuts import render, get_object_or_404, redirect
from .models import Formation, UE

# Create your views here.
def about(request):
    return render(request, "about.html")

def formation(request, id):
    fm = get_object_or_404(Formation, id=id)
    ues = UE.objects.filter(formations=fm)
    return render(request, "formation.html", {"formation": fm, "ues":ues})
