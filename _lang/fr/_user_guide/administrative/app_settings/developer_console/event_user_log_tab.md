---
nav_title: Journal d’événements utilisateurs
article_title: Journal d’événements utilisateurs
page_order: 2
page_type: reference
description: "Cet article de référence couvre le journal d’événements utilisateur, qui peut vous aider à déboguer ou à résoudre les problèmes dans votre intégration Braze."

---

# Journal d’événements utilisateurs

> Cet article de référence couvre le journal d’événements utilisateurs, y compris la façon d’accéder aux journaux et de les utiliser pour la résolution des problèmes. En plus de cet article, nous vous recommandons également de consulter notre cours d’apprentissage Braze [Outils d’assurance qualité et de débogage](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), qui explique comment utiliser le Journal d’événements utilisateurs pour effectuer votre propre débogage et résoudre vous-même les problèmes.

Le journal d’événements utilisateurs peut vous aider à analyser, déboguer ou résoudre les problèmes dans votre intégration Braze. Cet onglet vous fournit un journal des erreurs qui détaille le type d’erreur, l’application correspondante, le moment de la survenue et la possibilité d’afficher les données brutes associées.

Pour trouver facilement vos journaux, vous pouvez filtrer en fonction de :

* SDK ou API
* Noms des applications
* Plage temporelle
* Utilisateur

Chaque journal est divisé en plusieurs sections, qui peuvent inclure :

* Attributs de l’appareil
* Attributs utilisateur
* Événements
* Événements de campagne
* Données de réponse

Cliquez sur le bouton **Raw Data (Données brutes)** pour afficher les données JSON brutes pour ce journal spécifique.

![Journaux bruts pour les événements][10]

Les journaux d’événements utilisateurs resteront dans le tableau de bord pendant 30 jours après leur enregistrement.

## Résolution des problèmes

### Journaux SDK manquants pour les utilisateurs test

Si vous avez ajouté un utilisateur à un groupe interne, mais qu’il n’affiche aucun journal SDK dans le journal d’événements utilisateurs, cela peut être le résultat d’une option de configuration manquante. Pour recueillir les journaux SDK, assurez-vous de sélectionner **Record User Events for group members (Enregistrer les événements utilisateur pour les membres du groupe)** dans les **Internal Group Settings (Paramètres du groupe interne)** pour ce [groupe interne]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/).

### Retard dans les mises à jour des journaux

Ceci peut être une lenteur normale de la part de notre API.

Lorsque vous appelez des méthodes du SDK, celui-ci met généralement ces événements en cache localement et les transmet au serveur toutes les 10 secondes. Il peut s’écouler entre une seconde et quelques minutes avant que notre file d’attente de traitement des tâches n’ingère les événements, en fonction de la charge globale du moment.  

Si vous souhaitez que les événements arrivent le plus rapidement possible, essayez d’appeler la fonction `requestImmediateDataFlush()`.

### La fin de session et le début de session ont des horodatages similaires (iOS)

Le Journal d’événements utilisateurs affiche l’horodatage du moment où Braze a été notifié de la fin de la session, soit quelques millisecondes avant la prochaine session. Braze n’est pas en mesure de savoir que la session s’est terminée avant que l’application soit rouverte, car iOS est strict sur l’arrêt de l’exécution des threads lorsque l’application est en arrière-plan. Aucune donnée ne peut donc être remplacée par Braze tant que l’application n’est pas ouverte.

Alors que l’heure de fin de session sera spécifiée en secondes avant le début de la session, lorsque l’événement est supprimé, la durée de la session est supprimée séparément et est correcte - reflétant le temps d’ouverture de l’application. Par conséquent, ce comportement n’affecte pas le filtre `Durée de session médiane`.

En ce qui concerne les sessions utilisateur, vous pouvez utiliser Braze pour surveiller les données telles que :

- Le nombre de sessions d’un utilisateur 
- Quand un utilisateur a démarré une session pour la dernière fois 
- Si l’utilisateur commence une session après avoir reçu une campagne
- Quelle est la durée médiane de la session utilisateur

Ces comportements ne sont pas impactés par l’événement de fin de session qui est supprimé lors de la prochaine session.

[10]: {% image_buster /assets/img_archive/rawlogs.png %}
