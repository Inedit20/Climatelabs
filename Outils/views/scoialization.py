from django.db.models import fields
from django.db.models.aggregates import Max, Min
from django.db.models.expressions import ExpressionWrapper
from django.db.models.fields import IntegerField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.utils import translation
from django.views.generic import TemplateView
from django.utils import timezone
from django.utils.translation import ugettext
from django.views.generic import CreateView, ListView
from Outils.models import Evaluation, Role, EvalRoles, Afectation_Roles, Competance
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from django.db.models import Avg, Sum, F, Value, Count
from django.db.models.functions  import Length, Upper 
from django.http import JsonResponse
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from ..filters import  RolesFilter
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from Outils.utils import get_max_order


# eval c'est pur une evaluation 

#redirect('scoialization_results', pk=eval.pk)


# Fonction pour la selection des rôles individuels 
def roleList(request, pk):
    eval = get_object_or_404(Evaluation, pk=pk)
    evaluation = get_object_or_404(Evaluation, pk=pk)
    roles_definis = Competance.objects.all()
    roles= EvalRoles.objects.filter(eval=eval)
    return render(request, 'Scoialization/roles_selection.html', {'evaluation': evaluation, 'roles':roles, 'roles_definis':roles_definis, 'eval':eval })


def add_role(request, pk):
    eval = get_object_or_404(Evaluation, pk=pk)
    name = request.POST.get('rolename')
    # add role
    role = Role.objects.get_or_create(name=name)[0]
    # add the role to the evaluation's role list 
    if not EvalRoles.objects.filter(role=role, eval=eval).exists():
       EvalRoles.objects.create(
        role=role,
        eval=eval, 
        order=get_max_order(eval))
 
    roles= EvalRoles.objects.filter(eval=eval)
    messages.success(request, f"Added {name} to list of roles")
    return render(request, 'Scoialization/role-list.html', {'roles':roles, 'eval':eval})



#@require_http_methods(['DELETE'])
def delete_role(request, pk_1, pk_2):
    eval = get_object_or_404(Evaluation, pk=pk_1)
    EvalRoles.objects.get(pk=pk_2).delete()
    roles = EvalRoles.objects.filter(eval=eval)
    messages.success(request)
    return render(request, 'Scoialization/role-list.html', {'roles': roles, 'eval':eval})



def clear(request):
    return HttpResponse("")



def sort(request):
    role_pks_order = request.POST.getlist('role_order')
    roles = []
    for idx, role_pk in enumerate(role_pks_order, start=1):
        userrole = EvalRoles.objects.get(pk=role_pk)
        userrole.order = idx
        userrole.save()
        roles.append(userrole)
    messages.success(request)

    return render(request, 'Scoialization/role-list.html', {'roles': roles})






class IndexView(TemplateView):
    template_name = 'Scoialization/index.html'




# View pour la création du Profile de l'expert

def Scoialization_results(request, pk):
    eval= get_object_or_404(Evaluation, pk=pk)
    evaluation= get_object_or_404(Evaluation, pk=pk)
    template_name = 'Scoialization/resultats.html'
    affectation = Afectation_Roles.objects.filter(evaluation__pk= eval.pk)
    facilitador = evaluation.interculturel_1 + evaluation.mediation_1 + evaluation.moderation_1 + evaluation.moderation_2+evaluation.moderation_3+evaluation.participation_1+ evaluation.participation_2
    facilitador = facilitador/7
    visionario=   evaluation.technique_1+evaluation.pensee_1+evaluation.method_r_1+evaluation.method_r_2+evaluation.method_c_1
    maker = evaluation.gestion_projet_1+evaluation.gestion_projet_2+evaluation.evaluation_1+evaluation.organisation_1+evaluation.organisation_2
    manager = evaluation.esprit_1+ evaluation.esprit_2+evaluation.networking_1+evaluation.networking_2+evaluation.communication_1+evaluation.communication_2
    visionario = visionario/5
    maker= maker/5
    manager= manager/6
    my_list = [manager, maker, visionario, facilitador]
    V_t= manager+maker+visionario+facilitador
    if V_t != 0 :
        maker= (maker/V_t)*100
        manager= (manager/V_t)*100
        visionario =(visionario/V_t)*100
        facilitador= (facilitador/V_t)*100
   # my_list.sort()
    roles= EvalRoles.objects.filter(eval=eval)
    sujets= Evaluation.objects.filter(profile__equipe = eval.profile.equipe)
   # max_rating = MyMODEL.objects.aggregate(Max('rating'))
    #partie 1
    sujets_interculturel_1_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('interculturel_1')).get('interculturel_1__max')
    sujets_med_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('mediation_1')).get('mediation_1__max')
    sujets_mod_1_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('moderation_1')).get('moderation_1__max')
    sujets_mod_2_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('moderation_2')).get('moderation_2__max')
    sujets_mod_3_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('moderation_3')).get('moderation_3__max')
    sujets_participation_1_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('participation_1')).get('participation_1__max')
    sujets_participation_2_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('participation_2')).get('participation_2__max')
    #partie 2visionario
    sujets_technique_1_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('technique_1')).get('technique_1__max')
    sujets_pensee_1_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('pensee_1')).get('pensee_1__max')
    sujets_method_r_1_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('method_r_1')).get('method_r_1__max')
    sujets_method_r_2_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('method_r_2')).get('method_r_2__max')
    sujets_method_c_1_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('method_c_1')).get('method_c_1__max')
    #partie 3 Maker
    sujets_gestion_projet_1_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('gestion_projet_1')).get('gestion_projet_1__max')
    sujets_gestion_projet_2_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('gestion_projet_2')).get('gestion_projet_2__max')
    sujets_evaluation_1_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('evaluation_1')).get('evaluation_1__max')
    sujets_organisation_1_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('organisation_1')).get('organisation_1__max')
    sujets_organisation_2_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('organisation_2')).get('organisation_2__max')
    # partie 4 Manager
    sujets_gestion_esprit_1_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('esprit_1')).get('esprit_1__max')
    sujets_gestion_esprit_2_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('esprit_2')).get('esprit_2__max')
    sujets_networking_1_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('networking_1')).get('networking_1__max')
    sujets_networking_2_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('networking_2')).get('networking_2__max')
    sujets_communication_1_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('communication_1')).get('communication_1__max')
    sujets_communication_2_max= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Max('communication_2')).get('communication_2__max')
    #partie 1
    sujets_interculturel_1_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('interculturel_1')).get('interculturel_1__min')
    sujets_med_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('mediation_1')).get('mediation_1__min')
    sujets_mod_1_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('moderation_1')).get('moderation_1__min')
    sujets_mod_2_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('moderation_2')).get('moderation_2__min')
    sujets_mod_3_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('moderation_3')).get('moderation_3__min')
    sujets_participation_1_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('participation_1')).get('participation_1__min')
    sujets_participation_2_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('participation_2')).get('participation_2__min')
    #partie 2visionario
    sujets_technique_1_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('technique_1')).get('technique_1__min')
    sujets_pensee_1_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('pensee_1')).get('pensee_1__min')
    sujets_method_r_1_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('method_r_1')).get('method_r_1__min')
    sujets_method_r_2_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('method_r_2')).get('method_r_2__min')
    sujets_method_c_1_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('method_c_1')).get('method_c_1__min')
    #partie 3 Maker
    sujets_gestion_projet_1_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('gestion_projet_1')).get('gestion_projet_1__min')
    sujets_gestion_projet_2_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('gestion_projet_2')).get('gestion_projet_2__min')
    sujets_evaluation_1_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('evaluation_1')).get('evaluation_1__min')
    sujets_organisation_1_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('organisation_1')).get('organisation_1__min')
    sujets_organisation_2_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('organisation_2')).get('organisation_2__min')
    # partie 4 Manager
    sujets_gestion_esprit_1_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('esprit_1')).get('esprit_1__min')
    sujets_gestion_esprit_2_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('esprit_2')).get('esprit_2__min')
    sujets_networking_1_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('networking_1')).get('networking_1__min')
    sujets_networking_2_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('networking_2')).get('networking_2__min')
    sujets_communication_1_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('communication_1')).get('communication_1__min')
    sujets_communication_2_min= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Min('communication_2')).get('communication_2__min')



    #partie 1
    sujets_interculturel_1_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('interculturel_1')).get('interculturel_1__avg')
    sujets_med_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('mediation_1')).get('mediation_1__avg')
    sujets_mod_1_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('moderation_1')).get('moderation_1__avg')
    sujets_mod_2_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('moderation_2')).get('moderation_2__avg')
    sujets_mod_3_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('moderation_3')).get('moderation_3__avg')
    sujets_participation_1_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('participation_1')).get('participation_1__avg')
    sujets_participation_2_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('participation_2')).get('participation_2__avg')
    #partie 2visionario
    sujets_technique_1_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('technique_1')).get('technique_1__avg')
    sujets_pensee_1_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('pensee_1')).get('pensee_1__avg')
    sujets_method_r_1_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('method_r_1')).get('method_r_1__avg')
    sujets_method_r_2_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('method_r_2')).get('method_r_2__avg')
    sujets_method_c_1_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('method_c_1')).get('method_c_1__avg')
    #partie 3 Maker
    sujets_gestion_projet_1_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('gestion_projet_1')).get('gestion_projet_1__avg')
    sujets_gestion_projet_2_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('gestion_projet_2')).get('gestion_projet_2__avg')
    sujets_evaluation_1_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('evaluation_1')).get('evaluation_1__avg')
    sujets_organisation_1_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('organisation_1')).get('organisation_1__avg')
    sujets_organisation_2_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('organisation_2')).get('organisation_2__avg')
    # partie 4 Manager
    sujets_gestion_esprit_1_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('esprit_1')).get('esprit_1__avg')
    sujets_gestion_esprit_2_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('esprit_2')).get('esprit_2__avg')
    sujets_networking_1_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('networking_1')).get('networking_1__avg')
    sujets_networking_2_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('networking_2')).get('networking_2__avg')
    sujets_communication_1_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('communication_1')).get('communication_1__avg')
    sujets_communication_2_avg= Evaluation.objects.filter(profile__equipe = eval.profile.equipe).aggregate(Avg('communication_2')).get('communication_2__avg')   



    try:
        eval = get_object_or_404(Evaluation, pk=pk)
    except eval.DoesNotExist:
            raise Http404('evaluation does not exist')
    return render(request, template_name, {"sujets_technique_1_max":sujets_technique_1_max,"sujets_pensee_1_max":sujets_pensee_1_max,"sujets_method_r_1_max":sujets_method_r_1_max,"sujets_method_r_2_max":sujets_method_r_2_max,"sujets_method_c_1_max":sujets_method_c_1_max,
    "sujets_gestion_projet_1_max":sujets_gestion_projet_1_max,"sujets_gestion_projet_2_max": sujets_gestion_projet_2_max,"sujets_evaluation_1_max":sujets_evaluation_1_max,"sujets_organisation_1_max":sujets_organisation_1_max, "sujets_organisation_2_max":sujets_organisation_2_max,
    "sujets_interculturel_1_max":sujets_interculturel_1_max,"sujets_med_max":sujets_med_max,"sujets_mod_1_max": sujets_mod_1_max, "sujets_mod_2_max": sujets_mod_2_max,"sujets_mod_3_max": sujets_mod_3_max, "sujets_participation_1_max":sujets_participation_1_max,"sujets_participation_2_max":sujets_participation_2_max,
    "sujets_gestion_esprit_1_max":sujets_gestion_esprit_1_max,"sujets_gestion_esprit_2_max":sujets_gestion_esprit_2_max,"sujets_networking_1_max":sujets_networking_1_max,
    "sujets_networking_2_max":sujets_networking_2_max,"sujets_communication_1_max":sujets_communication_1_max,"sujets_communication_2_max":sujets_communication_2_max,
    "sujets_technique_1_min":sujets_technique_1_min,"sujets_pensee_1_min":sujets_pensee_1_min,"sujets_method_r_1_min":sujets_method_r_1_min,"sujets_method_r_2_min":sujets_method_r_2_min,"sujets_method_c_1_min":sujets_method_c_1_min,
    "sujets_gestion_projet_1_min":sujets_gestion_projet_1_min,"sujets_gestion_projet_2_min": sujets_gestion_projet_2_min,"sujets_evaluation_1_min":sujets_evaluation_1_min,"sujets_organisation_1_min":sujets_organisation_1_min, "sujets_organisation_2_min":sujets_organisation_2_min,
    "sujets_interculturel_1_min":sujets_interculturel_1_min,"sujets_med_min":sujets_med_min,"sujets_mod_1_min": sujets_mod_1_min, "sujets_mod_2_min": sujets_mod_2_min,"sujets_mod_3_min": sujets_mod_3_min, "sujets_participation_1_min":sujets_participation_1_min,"sujets_participation_2_min":sujets_participation_2_min,
    "sujets_gestion_esprit_1_min":sujets_gestion_esprit_1_min,"sujets_gestion_esprit_2_min":sujets_gestion_esprit_2_min,"sujets_networking_1_min":sujets_networking_1_min,
    "sujets_networking_2_min":sujets_networking_2_min,"sujets_communication_1_min":sujets_communication_1_min,"sujets_communication_2_min":sujets_communication_2_min,
    "sujets_technique_1_avg":sujets_technique_1_avg,"sujets_pensee_1_avg":sujets_pensee_1_avg,"sujets_method_r_1_avg":sujets_method_r_1_avg,"sujets_method_r_2_avg":sujets_method_r_2_avg,"sujets_method_c_1_avg":sujets_method_c_1_avg,
    "sujets_gestion_projet_1_avg":sujets_gestion_projet_1_avg,"sujets_gestion_projet_2_avg": sujets_gestion_projet_2_avg,"sujets_evaluation_1_avg":sujets_evaluation_1_avg,"sujets_organisation_1_avg":sujets_organisation_1_avg, "sujets_organisation_2_avg":sujets_organisation_2_avg,
    "sujets_interculturel_1_avg":sujets_interculturel_1_avg,"sujets_med_avg":sujets_med_avg,"sujets_mod_1_avg": sujets_mod_1_avg, "sujets_mod_2_avg": sujets_mod_2_avg,"sujets_mod_3_avg": sujets_mod_3_avg, "sujets_participation_1_avg":sujets_participation_1_avg,"sujets_participation_2_avg":sujets_participation_2_avg,
    "sujets_gestion_esprit_1_avg":sujets_gestion_esprit_1_avg,"sujets_gestion_esprit_2_avg":sujets_gestion_esprit_2_avg,"sujets_networking_1_avg":sujets_networking_1_avg,
    "sujets_networking_2_avg":sujets_networking_2_avg,"sujets_communication_1_avg":sujets_communication_1_avg,"sujets_communication_2_avg":sujets_communication_2_avg,
    "affectation":affectation, "eval" : eval, "evaluation": evaluation, "facilitador" : facilitador,'roles':roles, "visionario" : visionario, "maker" : maker, "manager": manager , "sujets": sujets, 'VT': V_t})

