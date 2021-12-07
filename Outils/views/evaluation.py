from django.db.models import fields
from django.db.models.expressions import ExpressionWrapper
from django.db.models.fields import IntegerField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.utils import timezone
from django.utils.translation import ugettext
from django.views.generic import CreateView, ListView
from Outils.models import Equipe, Evaluation, Question, Profile
from ..forms  import QuestionForm, FormulaireForm, ProfileForm, EquipeForm
#from  stories.filters import CasesFilter
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




# View pour la création du Profile de l'expert

def Home(request):
    if request.method == "POST" :
        form = ProfileForm (request.POST)
        if form.is_valid():
            profile= form.save(commit=False)
            #eval.date =timezone.now()
            profile.save()
            return redirect('formulaire', pk=profile.pk)
    else:
        form = ProfileForm()
    return render(request, 'Dash/index.html', {'form':form})

# View pour la création de l'équipe
def EquipeView(request):
    equipes= Equipe.objects.all()
    return render(request, 'Dash/Equipe/equipe.html', {'equipes':equipes})





# Equipe name 
def add_equipe(request):
    name = request.POST.get('equipename')
    # add equipe 
    equipe = Equipe.objects.create(name=name)
    # add the role to the evaluation's role list 
    #request.equipe.add(equipe)
    equipes= Equipe.objects.all()
    #messages.success(request, f"Added {name_equipe} to list of films")
    return render(request, 'Dash/Equipe/equipe-list.html', {'equipes':equipes})









# View pour la création du Profile de l'expert

def Profile_1(request, pk):
    equipe= get_object_or_404(Equipe, pk=pk)
    if request.method == "POST" :
        form = ProfileForm (request.POST)
        if form.is_valid():
            profile= form.save(commit=False)
            profile.equipe= equipe 
            #eval.date =timezone.now()
            profile.save()
            return redirect('formulaire', pk=profile.pk)
    else:
        form = ProfileForm()
    return render(request, 'Dash/profile.html', {'form':form})


# View pour la création formulaire

def Formulaire(request, pk):
    profile= get_object_or_404(Profile, pk=pk)
    if request.method == "POST" :
        form = FormulaireForm (request.POST)
        if form.is_valid():
            formulaire= form.save(commit=False)
            formulaire.created_date=timezone.now()
            formulaire.profile=profile
            formulaire.save()
            return redirect('scoialization', pk=formulaire.pk)
    else:
        form = FormulaireForm()
    return render(request, 'Dash/forms/evaluation.html', {'form':form})





def Formulaire_detail(request, pk, *args, **kwargs):
    evaluation= get_object_or_404(Evaluation, pk=pk)
    template_name = 'Dash/pages/forms/detail.html'

    return render(request, template_name, {"evaluation": evaluation})




def get_data(request, pk, *args, **kwargs):
    evaluation= get_object_or_404(Evaluation, pk=pk)
    labels= ["Intercluturel.1","Mediation.1","Modération.1", "Moderation.2", "Modération.3","Participation.1", "Participation.2",
                      "Technique.1", "Pensée.1","Methode.R1", "Methode.R2", "Methode.C1",  
                      "Gestion.1", "Gestion.2","Evaluation.1", "Autogestion.1", "Autogestion.2",
                      "Esprit.1", "Esprit.2","Networking.1","Networking.2", "Communication.1", "Communication.2"]
    default_items= [
        evaluation.interculturel_1,evaluation.mediation_1,evaluation.moderation_1,evaluation.moderation_2,evaluation.moderation_3,evaluation.participation_1, evaluation.participation_2,
        evaluation.technique_1,evaluation.pensee_1,evaluation.method_r_1, evaluation.method_r_2,evaluation.method_c_1,
        evaluation.gestion_projet_1,evaluation.gestion_projet_2,evaluation.evaluation_1,evaluation.organisation_1,evaluation.organisation_2,
        evaluation.esprit_1, evaluation.esprit_2,evaluation.networking_1,evaluation.networking_2,evaluation.communication_1,evaluation.communication_2]
    
    data = {
            "labels": labels,
            "default" : default_items,
            
        }
    return JsonResponse(data)






class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels= ["sales", "customers", "bn", "gjg"]
        default_items= [0.5,0.2,0.3,0.1]
        data = {
            "labels": labels,
            "default" : default_items,
            
        }
        return Response(data)

 


class New_Evaluation(CreateView):

    model= Question
    form_class = QuestionForm
    template_name = 'Pages/new_eval.html'

    def form_valid(self, form):
        com_form = form.save(commit=False)
        com_form.save()
        return redirect('calcul', com_form.pk)







class Evaluation(CreateView):

    model= Question
    form_class = QuestionForm
    template_name = 'Pages/new_eval.html'

    def form_valid(self, form):
        com_form = form.save(commit=False)
        com_form.save()
        return redirect('calcul', com_form.pk)

















def calcul(request, pk):
    labels = []
    data = []
    data_comp= []
    labels_comp=[]

#  a=[1,2,3,4,5]

# median= np.median(a, axis=0)

    query_1 = Question.objects.values('Q_1')
    for question in query_1:
        data_comp.append(question['Q_1'])
    
    median= np.median( data_comp, axis=0)

    query_set= get_object_or_404(Question, pk=pk)
    data= [query_set.Q_1,query_set.Q_2,query_set.Q_3]
    return render(request, 'Pages/calcul.html', {'labels':labels, 'data':data, 'query_median':query_set, 'median': median, 'data_comp':data_comp  })

  
def calcul_chart(request):
    labels= []
    data = []

    query_median= Question.objects.values('Q1').annotate(avg=F('Q_1')).order_by('title')
    for med in query_median:
        labels.append(med['title'])
        data.append(med['avg'])

    return JsonResponse (data={
            'labels':labels,
            'data': data,

        })