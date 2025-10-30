---
nav_title: Journal des événements utilisateurs
article_title: Journal des événements utilisateurs
page_order: 7
page_type: reference
description: "Cet article de référence traite du journal des événements utilisateurs, qui peut vous aider à déboguer ou à résoudre des problèmes dans votre intégration Braze."

---

# Journal des événements utilisateurs

> Le journal des événements utilisateurs peut vous aider à décomposer, déboguer ou résoudre les problèmes de votre intégration Braze. Cet onglet vous présente un journal des erreurs qui détaille le type d'erreur, l'application à laquelle elle est associée, le moment où elle s'est produite et, souvent, la possibilité d'afficher les données brutes qui y sont associées.

{% alert tip %}
Outre cet article, nous vous recommandons également de consulter notre cours d'apprentissage sur l ['assurance qualité et les outils de débogage](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) Braze, qui explique comment utiliser le journal des événements utilisateurs pour effectuer vos propres opérations de résolution des problèmes et de débogage.
{% endalert %}

Pour accéder au journal, allez dans **Paramètres** > Journal des événements utilisateurs.

Pour retrouver facilement vos logs, vous pouvez les filtrer en fonction de :

* SDK ou API
* Noms des applications
* Délai
* Utilisateur

Chaque journal est divisé en plusieurs sections, qui peuvent inclure

* Attributs de l'appareil
* Attributs de l'utilisateur
* Evénements
* Événements de la campagne
* Données de réponse

Sélectionnez l'icône **Développer les données** pour afficher les données JSON brutes de ce journal spécifique.

\![L'icône "Développer les données" à côté d'un journal spécifique.]({% image_buster /assets/img_archive/expand_data.png %})

Les journaux des événements utilisateurs resteront dans le tableau de bord pendant 30 jours après leur enregistrement.

\![Journaux bruts pour les événements]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## Résolution des problèmes

### Absence de journaux SDK pour les utilisateurs test

Si vous avez ajouté un utilisateur à un groupe interne, mais qu'il n'affiche aucun journal SDK dans le journal des événements utilisateurs, cela peut être dû à une option de configuration manquante. Pour capturer les journaux des SDK, assurez-vous de sélectionner **Enregistrer les événements utilisateurs pour les membres du groupe** dans les **Paramètres du groupe interne** pour ce [groupe interne]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/).

### Retard dans la mise à jour des journaux

Il s'agit potentiellement d'une lenteur normale de la part de notre API.

Lorsque vous appelez des méthodes du SDK, celui-ci met généralement ces événements en cache localement et les transmet au serveur toutes les 10 secondes. Notre file d'attente de traitement des tâches peut prendre entre une seconde et quelques minutes pour ingérer les événements, en fonction de la charge globale du moment.  

Si vous souhaitez que les événements arrivent le plus rapidement possible, essayez d'appeler la fonction `requestImmediateDataFlush()`.

### La fin et le début de la session ont des horodatages similaires (iOS)

Le journal des événements utilisateurs indique l'heure à laquelle Braze a été informé de la fin de la session, soit quelques millisecondes avant le début de la prochaine session. Braze n'est pas en mesure de savoir que la session est terminée avant la réouverture de l'application, car iOS est agressif en ce qui concerne l'arrêt de l'exécution des threads lorsque l'application est en arrière-plan - aucune donnée ne peut donc être transmise à Braze tant que l'application n'est pas rouverte.

Alors que l'heure de fin de session sera spécifiée en secondes avant le début de la session, lorsque l'événement est nettoyé, la durée de la session est nettoyée séparément et est correcte, reflétant l'heure à laquelle l'application a été ouverte. Par conséquent, ce comportement n'a pas d'incidence sur le filtre `Median Session Duration`.

En ce qui concerne les sessions d'utilisateurs, vous pouvez utiliser Braze pour contrôler des données telles que :

- Nombre de sessions d'un utilisateur
- Date à laquelle un utilisateur a démarré une session pour la dernière fois
- Si l'utilisateur démarre une session après avoir reçu une campagne
- Durée médiane de la session de l'utilisateur

Ces comportements ne sont pas affectés par la vidange de l'événement de fin de session lors de la session suivante.

