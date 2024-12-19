from django.shortcuts import render, get_object_or_404, redirect
from .models import Formation, UE
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#### Q19 ####

# Il faut ajouter @login_required à toutes les pages. q19

## Il faut ajouter ça aux fonction d'ajouts, modification, suppression de UE -> pour gerer les autorisations:

# responsables =  []
# fms = Formation.objects.all()
# for fm in fms:
	# if not fm.responsable in responsables:
		# responsables.append(fm.responsable)

# if not request.user in responsables and not request.user.is_superuser:
	# return HttpResponse('Unauthorized', status=401)

## Il faut ajouter ça après le code précédent juste dans la fonction de modification:

# ue = get_object_or_404(UE, id=id)
# if not request.user in ue.responsables.all():
	# return HttpResponse('Unauthorized', status=401)

#### Q19 ####

@login_required
def about(request):
    return render(request, "about.html")

@login_required
def formation(request, id):
    fm = get_object_or_404(Formation, id=id)
    ues = UE.objects.filter(formations=fm)
    return render(request, "formation.html", {"formation": fm, "ues":ues})

@login_required
def ue_view(request, id):
    u = get_object_or_404(UE, id=id)
    return render(request, "ue_view.html", {"ue":u})

@login_required
def formations(request):
    fm = Formation.objects.all()
    return render(request, "formations.html", {"fm":fm})

@login_required
def ues(request):
    ues = UE.objects.all()
    return render(request, "ues.html", {"ues":ues})


@login_required
def exclusive(request): #q20)
    responsables =  []
    fms = Formation.objects.all()
    for fm in fms:
        if not fm.responsable in responsables:
            responsables.append(fm.responsable)

    if not request.user in responsables and not request.user.is_superuser:
        return HttpResponse('Unauthorized', status=401)

    ues = UE.objects.all()

    data = []
    for formation in fms:
        ue_attaches = UE.objects.filter(formations=formation)
        nombre_ue_attache = ue_attaches.count()
        responsables_noms =  []

        volume_total_cm = 0
        volume_total_td = 0
        volume_total_tp = 0
        volume_total_credits = 0

        for ue_attache in ue_attaches:
            for r in ue_attache.responsables.all():
                responsables_noms.append(r.last_name + " " + r.first_name)

            volume_total_cm = ue_attache.CM
            volume_total_td = ue_attache.TD
            volume_total_tp = ue_attache.TP
            volume_total_credits = ue_attache.credits

        volume_total_heures_equivalent_cm = volume_total_cm / 1.5 ## 1h de CM compte 1h30

        data.append({
            "id": formation.id,
            "intitule": formation.intitule,
            "nombre_ue_attache": nombre_ue_attache,
            "responsables": sorted(responsables_noms),
            "volume_total_cm": volume_total_cm,
            "volume_total_td": volume_total_td,
            "volume_total_tp": volume_total_tp,
            "volume_total_credits": volume_total_credits,
            "volume_total_heures_equivalent_cm": volume_total_heures_equivalent_cm
        })

    return render(request, "exclusive.html", {"data": data})