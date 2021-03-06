# Generated by Django 3.0 on 2021-12-01 15:38

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Compétance name')),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255, unique=True)),
                ('organisme', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'ordering': [django.db.models.functions.text.Lower('name')],
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gestion_projet_1', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Concevoir et mettre en œuvre des projets à caractère innovant')),
                ('gestion_projet_2', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Répondre aux exigences techniques, financières et juridiques des projets')),
                ('moderation_1', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name="Élaborer des stratégies émergentes pour intégrer les nouvelles connaissances et piloter l'ensemble du projet en temps réel")),
                ('moderation_2', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Aider à dessiner une vision collective, encourager les gens à partager des idées et à participer')),
                ('moderation_3', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Appliquer des méthodes et pratiques pédagogiques  pour assurer la progression des équipes et des participants')),
                ('mediation_1', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Concevoir et mettre en œuvre des stratégies de résolution des conflits')),
                ('networking_1', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Établir des liens et des relations avec les organisations et les entreprises locales, les organismes de financement, des associations')),
                ('networking_2', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Favoriser des rencontres pertinentes et fructueuse entre les personnes')),
                ('participation_1', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Repenser les modèles de projets traditionnels sur la base des approches participatives courantes')),
                ('participation_2', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Mettre en place des dispositifs collaboratifs pour inviter les gens à participer aux activités du projet, les familiariser avec le projet, les accueillir et les orienter')),
                ('communication_1', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name="Avoir de l'empathie et être ouvert aux autres points de vue en écoutant l'expérience des autres")),
                ('communication_2', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Utiliser les médias avec un style clair, positif et convivial')),
                ('organisation_1', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Croire en sa propre capacité à choisir une approche efficace pour mener à bien une tâche ou une activité dans des environnements de plus en plus complexes')),
                ('organisation_2', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Faire preuve de tolérance dans des situations de plus en plus complexes et contrariantes?')),
                ('interculturel_1', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name="Mettre en place des dispositifs permettant d'assurer l'inclusion de tous, quels que soient leur culture, leur âge, leur situation économique ou leur lieu de résidence")),
                ('evaluation_1', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name="Concevoir et mettre en œuvre des mécanismes de saisie et d'analyse des données afin d'éclairer une stratégie donnée et de mettre en évidence ses résultats")),
                ('method_r_1', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name="Travailler avec d'autres disciplines/acteurs de l'écosystème social")),
                ('method_r_2', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Appliquer des méthodes de travail/recherche différentes de celles utilisées dans ma discipline')),
                ('method_c_1', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name="Associer les idées et les connaissances de manière inédite, utiliser les techniques de design pour l'innovation")),
                ('technique_1', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Développer des prototypes technologiques appliqués via la programmation, la simulation, la modélisation, etc.')),
                ('esprit_1', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Gérer une entreprise ou une activité entrepreneuriale.')),
                ('esprit_2', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name="Recombiner les atouts et les opportunités dans le cadre d'un processus d'incubation de projet")),
                ('pensee_1', models.IntegerField(choices=[(0, '0 : Je ne comprends pas en quoi consiste la compétence.'), (1, '1 : Je comprends en quoi consiste la compétence et pourquoi elle est importante, mais je ne la pratique pas.'), (2, '2 : Je pratique cette compétence sous supervision ou avec de l encouragement. '), (3, '3 : Je pratique cette compétence sans supervision ni encouragement '), (4, '4 : J encourage ou je supervise les autres dans cette compétence. '), (5, '5 : J encourage ou je supervise les autres dans cette compétence. ')], default=0, verbose_name='Concevoir et mettre en œuvre des stratégies pour gérer la complexité, la pensée anticipative, et la culture du changement')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField(null=True)),
                ('title', models.CharField(max_length=200)),
                ('Q_1', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, verbose_name='Question1')),
                ('Q_2', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, verbose_name='Question2')),
                ('Q_3', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, verbose_name='Question3')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('eval', models.ManyToManyField(related_name='roles', to='Outils.Evaluation')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nom_prenom', models.CharField(max_length=200, verbose_name='Prénom et Nom ')),
                ('organisation', models.CharField(max_length=255)),
                ('statut', models.CharField(choices=[('chercheur', 'Chercheur'), ('labManager', 'Lab Manager'), ('technicien', 'Technicien'), ('stagiaire', 'Stagiaire'), ('professeur', 'Professeur'), ('directeur', 'Directeur')], max_length=255, verbose_name='Quel est votre statut au sein de votre tiers-lieu?')),
                ('mission', models.CharField(max_length=255)),
                ('domaine', models.CharField(max_length=255)),
                ('equipe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Outils.Equipe')),
            ],
        ),
        migrations.AddField(
            model_name='evaluation',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Outils.Profile'),
        ),
        migrations.CreateModel(
            name='EvalRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField()),
                ('eval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Outils.Evaluation')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Outils.Role')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Afectation_Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_1', models.IntegerField(choices=[(0, 'Manager'), (1, 'Maker'), (2, 'Facilitator'), (3, 'Visionnaire')], default=0, verbose_name='Concevoir et mettre en œuvre des stratégies pour gérer la complexité, la pensée anticipative, et la culture du changement')),
                ('role_2', models.IntegerField(choices=[(0, 'Manager'), (1, 'Maker'), (2, 'Facilitator'), (3, 'Visionnaire')], default=0, verbose_name='Concevoir et mettre en œuvre des stratégies pour gérer la complexité, la pensée anticipative, et la culture du changement')),
                ('role_3', models.IntegerField(choices=[(0, 'Manager'), (1, 'Maker'), (2, 'Facilitator'), (3, 'Visionnaire')], default=0, verbose_name='Concevoir et mettre en œuvre des stratégies pour gérer la complexité, la pensée anticipative, et la culture du changement')),
                ('role_4', models.IntegerField(choices=[(0, 'Manager'), (1, 'Maker'), (2, 'Facilitator'), (3, 'Visionnaire')], default=0, verbose_name='Concevoir et mettre en œuvre des stratégies pour gérer la complexité, la pensée anticipative, et la culture du changement')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Outils.Evaluation')),
            ],
        ),
    ]
