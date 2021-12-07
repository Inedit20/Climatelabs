
from django.urls import include, path
from .views import home, evaluation, scoialization


urlpatterns = [
    
    path('', evaluation.Home, name='home'),
    path('new_evaluation', evaluation.New_Evaluation.as_view(), name='new_eval'),
    path('join_evaluation', evaluation.Evaluation.as_view(), name='evaluation'),

    path('scoialization_results/<int:pk>', scoialization.Scoialization_results, name='scoialization_results'),
    path('guide', home.Guide, name='guide'),
    path('calcul/<int:pk>', evaluation.calcul, name='calcul'),
    path('api/data/<int:pk>', evaluation.get_data, name='api-data'),
    path('calcul/chart', evaluation.calcul_chart, name='population-chart'),
    path('team/', evaluation.EquipeView, name='equipe'),
    path('team/profil/<int:pk>', evaluation.Profile_1, name='profile' ),
    path('team/profil/evaluation/<int:pk>', evaluation.Formulaire, name='formulaire'),
    path('team/profil/evaluation/roles/<int:pk>', scoialization.roleList, name='scoialization'),
    path('evaluation/detail/<int:pk>/', evaluation.Formulaire_detail, name='detail'),
    path('api/chart/data', evaluation.ChartData.as_view()),
    path('index/', scoialization.IndexView.as_view(), name='index'),
    path('doc/', home.documentation, name='doc'),
    path('roles/', home.roles, name='roles'),



]



htmx_urlpatterns = [

    path('add-role/<int:pk>', scoialization.add_role, name='add-role'),
    path('add-equipe/', evaluation.add_equipe, name='add-equipe'),
    path('delete-role/<int:pk_1>/<int:pk_2>', scoialization.delete_role, name='delete-role'),
    path('sort/', scoialization.sort, name='sort'),
    path('clear/', scoialization.clear, name='clear'),

]

urlpatterns += htmx_urlpatterns





