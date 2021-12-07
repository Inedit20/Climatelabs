

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.db.models import fields
from django.forms.utils import ValidationError
from Outils.models import (Equipe, Question, Evaluation, Profile, Role, Afectation_Roles )
from django.forms import ModelChoiceField, widgets
from django.forms import ModelMultipleChoiceField
from django.forms import ModelForm
from django.utils.translation import ugettext

from django.utils.safestring import mark_safe

from django.utils.safestring import mark_safe


class QuestionForm(ModelForm):

    class Meta:
           model = Question
           fields = ['text','title','Q_1','Q_2','Q_3']
           widgets = {
               'Q_1': forms.RadioSelect(attrs={'class': 'inline'}),
               'Q_2': forms.RadioSelect(attrs={'class': 'inline'}),
               'Q_3': forms.RadioSelect(attrs={'class': 'inline'}),
           }  




class EquipeForm(ModelForm):

    class Meta: 
         model = Equipe
         fields= '__all__'



class FormulaireForm(ModelForm):

    class Meta:
        model= Evaluation
        fields=('gestion_projet_1','gestion_projet_2', 'moderation_1','moderation_2', 'moderation_3','mediation_1','networking_1','networking_2','participation_1','participation_2','communication_1','communication_2','organisation_1','organisation_2','interculturel_1','evaluation_1','method_r_1','method_r_2','method_c_1','technique_1','esprit_1','esprit_2','pensee_1')
        widgets = {
               'gestion_projet_1': forms.RadioSelect(attrs={'id': 'value'}),
               'gestion_projet_2': forms.RadioSelect(),
               'mediation_1': forms.RadioSelect(),
               'moderation_1': forms.RadioSelect(attrs={'class': 'inline'}),
               'moderation_2': forms.RadioSelect(attrs={'class': 'inline'}),
               'moderation_3': forms.RadioSelect(attrs={'class': 'inline'}),
               'networking_1': forms.RadioSelect(attrs={'class': 'inline'}),
               'networking_2': forms.RadioSelect(attrs={'class': 'inline'}),
               'participation_1': forms.RadioSelect(attrs={'class': 'inline'}),
               'participation_2': forms.RadioSelect(attrs={'class': 'inline'}),
               'communication_1': forms.RadioSelect(attrs={'class': 'inline'}),
               'communication_2': forms.RadioSelect(attrs={'class': 'inline'}),
               'organisation_1': forms.RadioSelect(attrs={'class': 'inline'}),
               'organisation_2': forms.RadioSelect(attrs={'class': 'inline'}),
               'interculturel_1': forms.RadioSelect(attrs={'class': 'inline'}),
               'evaluation_1': forms.RadioSelect(attrs={'class': 'inline'}),
               'method_r_1': forms.RadioSelect(attrs={'class': 'inline'}),
               'method_r_2': forms.RadioSelect(attrs={'class': 'inline'}),
               'method_c_1': forms.RadioSelect(attrs={'class': 'inline'}),
               'technique_1': forms.RadioSelect(attrs={'class': 'inline'}),
               'esprit_1': forms.RadioSelect(attrs={'class': 'inline'}),
               'esprit_2': forms.RadioSelect(attrs={'class': 'inline'}),
               'pensee_1': forms.RadioSelect(attrs={'class': 'inline'}),


           }  




class ProfileForm(ModelForm):

    class Meta:
        model= Profile
        fields=('email','nom_prenom','organisation','statut','mission','domaine')
