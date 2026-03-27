---
nav_title: Journal des événements utilisateurs
article_title: Journal des événements utilisateurs
page_order: 7
page_type: reference
description: "Cet article de référence couvre le journal des événements utilisateurs, qui peut vous aider à déboguer ou à résoudre les problèmes dans votre intégration Braze."

---

# Journal des événements utilisateurs

> Le journal des événements utilisateurs peut vous aider à analyser, déboguer ou résoudre les problèmes dans votre intégration Braze. Cet onglet vous fournit un journal des erreurs qui détaille le type d'erreur, l'application correspondante, le moment de la survenue et, souvent, la possibilité d'afficher les données brutes associées.

{% alert tip %}
Outre cet article, nous vous recommandons également de consulter notre cours d'apprentissage Braze sur l'[assurance qualité et les outils de débogage](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), qui explique comment utiliser le journal des événements utilisateurs pour effectuer vos propres opérations de résolution des problèmes et de débogage.
{% endalert %}

Pour accéder au journal, sélectionnez **Paramètres** > **Journal des événements utilisateurs**.

Pour trouver facilement vos journaux, vous pouvez filtrer en fonction de :

* SDK ou API
* Noms des applications
* Plage temporelle
* Utilisateur

Chaque journal est divisé en plusieurs sections, qui peuvent inclure :

* Attributs de l'appareil
* Attributs utilisateur
* Événements
* Événements de campagne
* Données de réponse

Sélectionnez l'icône **Développer les données** pour afficher les données JSON brutes de ce journal spécifique.

![L'icône « Développer les données » à côté d'un journal spécifique.]({% image_buster /assets/img_archive/expand_data.png %})

Les journaux des événements utilisateurs resteront dans le tableau de bord pendant 30 jours après leur enregistrement.

![Journaux bruts pour les événements]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## Résolution des problèmes

### Journaux SDK manquants pour les utilisateurs test

Si vous avez ajouté un utilisateur à un groupe interne, mais qu'il n'affiche aucun journal SDK dans le journal des événements utilisateurs, cela peut être dû à une option de configuration manquante. Pour capturer les journaux SDK, veillez à sélectionner **Enregistrer les événements utilisateurs pour les membres du groupe** dans les **Paramètres du groupe interne** du [groupe interne]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/) en question.

### Retard dans les mises à jour des journaux

Ceci peut être dû à une lenteur normale de notre API.

Lorsque vous appelez des méthodes du SDK, celui-ci met généralement ces événements en cache localement et les transmet au serveur toutes les 10 secondes. Il peut s'écouler entre une seconde et quelques minutes avant que notre file d'attente de traitement des tâches n'ingère les événements, en fonction de la charge globale du moment.  

Si vous souhaitez que les événements arrivent le plus rapidement possible, essayez d'appeler la fonction `requestImmediateDataFlush()`.

### Échecs d'impression des messages in-app

Si un message in-app ne s'affiche pas, vous pouvez en trouver la raison dans le journal des événements utilisateurs en développant les données JSON brutes de la requête SDK concernée et en recherchant le champ `error_code` dans la réponse. Le `error_code` identifie la raison précise de l'échec de l'impression (par exemple, une valeur de couleur invalide ou un problème de rendu). Partagez ce code d'erreur avec l'[assistance Braze]({{site.baseurl}}/braze_support/) si une investigation plus approfondie est nécessaire.

### La fin de session et le début de session ont des horodatages similaires (iOS)

Le journal des événements utilisateurs affiche l'horodatage du moment où Braze a été notifié de la fin de la session, soit quelques millisecondes avant le début de la session suivante. Braze n'est pas en mesure de savoir que la session s'est terminée avant que l'application soit rouverte, car iOS interrompt de manière stricte l'exécution des threads lorsque l'application est en arrière-plan. Aucune donnée ne peut donc être transmise à Braze tant que l'application n'est pas rouverte.

Bien que l'heure de fin de session soit indiquée en secondes avant le début de la session, lorsque l'événement est transmis, la durée de la session est envoyée séparément et reste correcte — elle reflète le temps pendant lequel l'application était ouverte. Par conséquent, ce comportement n'affecte pas le filtre `Median Session Duration`.

En ce qui concerne les sessions utilisateur, vous pouvez utiliser Braze pour surveiller des données telles que :

- Le nombre de sessions d'un utilisateur
- Quand un utilisateur a démarré une session pour la dernière fois
- Si l'utilisateur commence une session après avoir reçu une campagne
- Quelle est la durée médiane de la session utilisateur

Ces comportements ne sont pas impactés par l'événement de fin de session transmis lors de la session suivante.