from django.contrib.auth.models import AbstractUser
from django.db.models.expressions import OrderBy
from django.db.models.fields import EmailField
from tinymce.models import HTMLField
from django.db import models
from django.utils.html import escape, mark_safe
from django.dispatch import receiver
from django.utils import timezone
from djrichtextfield.widgets import RichTextWidget
from djrichtextfield.models import RichTextField
from django.utils.translation import ugettext_lazy
from django import forms
from django.forms.widgets import RadioSelect
from django.db.models.functions import Lower
import uuid



q_1_CHOICES = [(0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')]
q_2_CHOICES = [(0,'0'),(1,'1'),(2,'2'), (3,'3'),(4,'4'),(5,'5')]
q_3_CHOICES = [(0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')]




class Equipe(models.Model):
    name= models.TextField(max_length=255, blank=False, unique=True)
    organisme=models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
       
    class Meta:
        ordering= [Lower('name')]
    



class Profile(models.Model):
   equipe= models.ForeignKey(Equipe, on_delete=models.PROTECT)
   statut_list=[("chercheur","Chercheur"),("labManager","Lab Manager"),("technicien","Technicien"),("stagiaire","Stagiaire"),("professeur","Professeur"),("directeur","Directeur")]
   inter_CHOICES = [(0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')]
   email=EmailField()
   nom_prenom= models.CharField(verbose_name="Prénom et Nom ", max_length=200)
   organisation= models.CharField(max_length=255)
   statut= models.CharField(choices=statut_list,  max_length=255,verbose_name="Quel est votre statut au sein de votre tiers-lieu?", blank=False)
   mission= models.CharField(max_length=255)
   domaine=models.CharField(max_length=255)




class Evaluation(models.Model):
   profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
   inter_CHOICES = [(0,'0 : Je ne comprends pas en quoi consiste la compétence.'),(1,'1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'),(2,'2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '),(3,'3 : Je pratique cette compétence sans supervision ni encouragement '),(4,'4 : J encourage ou je supervise les autres dans cette compétence. '),(5,'5 : J encourage ou je supervise les autres dans cette compétence. ')]
   gestion_projet_1= models.IntegerField(choices=inter_CHOICES,verbose_name="Concevoir et mettre en œuvre des projets à caractère innovant", default=0)
   gestion_projet_2=models.IntegerField(choices=inter_CHOICES, verbose_name="Répondre aux exigences techniques, financières et juridiques des projets", default=0 )
   moderation_1=models.IntegerField(choices=inter_CHOICES, verbose_name="Élaborer des stratégies émergentes pour intégrer les nouvelles connaissances et piloter l'ensemble du projet en temps réel", default=0 )
   moderation_2=models.IntegerField(choices=inter_CHOICES, verbose_name="Aider à dessiner une vision collective, encourager les gens à partager des idées et à participer" , default=0 )
   moderation_3=models.IntegerField(choices=inter_CHOICES, verbose_name="Appliquer des méthodes et pratiques pédagogiques  pour assurer la progression des équipes et des participants", default=0  )
   mediation_1=models.IntegerField(choices=inter_CHOICES, verbose_name="Concevoir et mettre en œuvre des stratégies de résolution des conflits" , default=0 )
   networking_1 = models.IntegerField(choices=inter_CHOICES, verbose_name="Établir des liens et des relations avec les organisations et les entreprises locales, les organismes de financement, des associations", default=0  )
   networking_2= models.IntegerField(choices=inter_CHOICES, verbose_name="Favoriser des rencontres pertinentes et fructueuse entre les personnes", default=0  )
   participation_1= models.IntegerField(choices=inter_CHOICES, verbose_name="Repenser les modèles de projets traditionnels sur la base des approches participatives courantes", default=0 )
   participation_2= models.IntegerField(choices=inter_CHOICES, verbose_name="Mettre en place des dispositifs collaboratifs pour inviter les gens à participer aux activités du projet, les familiariser avec le projet, les accueillir et les orienter", default=0  )
   communication_1 = models.IntegerField(choices=inter_CHOICES, verbose_name="Avoir de l'empathie et être ouvert aux autres points de vue en écoutant l'expérience des autres" , default=0 )
   communication_2 = models.IntegerField(choices=inter_CHOICES, verbose_name="Utiliser les médias avec un style clair, positif et convivial", default=0  )
   organisation_1 = models.IntegerField(choices=inter_CHOICES, verbose_name="Croire en sa propre capacité à choisir une approche efficace pour mener à bien une tâche ou une activité dans des environnements de plus en plus complexes", default=0  )
   organisation_2 = models.IntegerField(choices=inter_CHOICES, verbose_name="Faire preuve de tolérance dans des situations de plus en plus complexes et contrariantes?", default=0  )
   interculturel_1 = models.IntegerField(choices=inter_CHOICES, verbose_name="Mettre en place des dispositifs permettant d'assurer l'inclusion de tous, quels que soient leur culture, leur âge, leur situation économique ou leur lieu de résidence" , default=0 )
   evaluation_1 = models.IntegerField(choices=inter_CHOICES, verbose_name="Concevoir et mettre en œuvre des mécanismes de saisie et d'analyse des données afin d'éclairer une stratégie donnée et de mettre en évidence ses résultats", default=0  )
   method_r_1 = models.IntegerField(choices=inter_CHOICES, verbose_name="Travailler avec d'autres disciplines/acteurs de l'écosystème social", default=0  )
   method_r_2= models.IntegerField(choices=inter_CHOICES, verbose_name="Appliquer des méthodes de travail/recherche différentes de celles utilisées dans ma discipline", default=0  )
   method_c_1= models.IntegerField(choices=inter_CHOICES, verbose_name="Associer les idées et les connaissances de manière inédite, utiliser les techniques de design pour l'innovation", default=0  )
   technique_1= models.IntegerField(choices=inter_CHOICES, verbose_name="Développer des prototypes technologiques appliqués via la programmation, la simulation, la modélisation, etc.", default=0 )
   esprit_1= models.IntegerField(choices=inter_CHOICES, verbose_name="Gérer une entreprise ou une activité entrepreneuriale." , default=0 )
   esprit_2= models.IntegerField(choices=inter_CHOICES, verbose_name="Recombiner les atouts et les opportunités dans le cadre d'un processus d'incubation de projet", default=0  )
   pensee_1=models.IntegerField(choices=inter_CHOICES, verbose_name="Concevoir et mettre en œuvre des stratégies pour gérer la complexité, la pensée anticipative, et la culture du changement", default=0 )
   created_date = models.DateTimeField(default=timezone.now)





class Competance(models.Model):
    name= models.CharField(max_length=200, verbose_name="Compétance name", blank= False )
    
    def __str__(self):
        return self.name




class Role(models.Model):
  name= models.CharField(max_length=150, verbose_name="name" )
  eval= models.ManyToManyField(Evaluation, related_name='roles', through='EvalRoles')

# through='EvalRoles'
  
  def __str__(self):
      return self.name



class EvalRoles(models.Model):
    eval=models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    role= models.ForeignKey(Role, on_delete= models.CASCADE)
    order= models.PositiveSmallIntegerField()
 

    class Meta:
        ordering = ['order']
    





class Question(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField(null=True)
    title = models.CharField(max_length=200)
    Q_1= models.IntegerField(choices=q_1_CHOICES,  verbose_name='Question1', default=0)
    Q_2= models.IntegerField(choices=q_2_CHOICES, verbose_name='Question2', default=0)
    Q_3= models.IntegerField(choices=q_3_CHOICES, verbose_name='Question3', default=0)
    

    def __str__(self):
        return self.title
class Afectation_Roles (models.Model):
   inter_CHOICES = [(0,'Manager'),(1,'Maker'),(2,'Facilitator'),(3,'Visionnaire')]
   evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE )
   role_1= models.IntegerField(choices=inter_CHOICES, verbose_name="Concevoir et mettre en œuvre des stratégies pour gérer la complexité, la pensée anticipative, et la culture du changement", default=0 )
   role_2=  models.IntegerField(choices=inter_CHOICES, verbose_name="Concevoir et mettre en œuvre des stratégies pour gérer la complexité, la pensée anticipative, et la culture du changement", default=0 )
   role_3= models.IntegerField(choices=inter_CHOICES, verbose_name="Concevoir et mettre en œuvre des stratégies pour gérer la complexité, la pensée anticipative, et la culture du changement", default=0 )
   role_4=  models.IntegerField(choices=inter_CHOICES, verbose_name="Concevoir et mettre en œuvre des stratégies pour gérer la complexité, la pensée anticipative, et la culture du changement", default=0 )
   created_date = models.DateTimeField(default=timezone.now)
   


