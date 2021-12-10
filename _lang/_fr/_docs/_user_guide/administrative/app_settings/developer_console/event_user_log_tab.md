---
nav_title: Onglet du journal de l'utilisateur de l'événement
article_title: Onglet du journal de l'utilisateur de l'événement
page_order: 2
page_type: Référence
description: "Cet article de référence couvre le journal Event User Log, qui peut vous aider à déboguer ou à résoudre des problèmes dans votre intégration à Braze."
---

# Onglet du journal de l'utilisateur de l'événement

Le journal des utilisateurs des événements peut vous aider à vous décomposer, déboguer ou résoudre des problèmes dans votre intégration de Braze. Cet onglet vous donne un journal d'erreurs qui détaille le type d'erreur, à quelle application il est associé, quand cela s'est produit, et souvent une occasion de voir les données brutes qui lui sont associées.

Pour trouver facilement vos logs, vous pouvez filtrer en fonction de :

* SDK ou API
* Noms des applications
* Intervalle de temps
* Utilisateur

Chaque log est divisé en plusieurs sections, qui peuvent inclure :

* Attributs de l'appareil
* Attributs de l'utilisateur
* Évènements
* Événements de la campagne
* Données de réponse

Cliquer sur le bouton **Données brutes** pour afficher les données JSON brutes pour ce journal spécifique.

!\[Journal brut\]\[10\]

Les journaux des utilisateurs d'événements resteront dans le tableau de bord pendant 30 jours après qu'ils soient enregistrés.

## Dépannage

### Journaux SDK manquants pour les utilisateurs de test

Si vous avez ajouté un utilisateur à un groupe interne, mais qu'il ne montre aucun log SDK dans le journal de l'utilisateur de l'événement, ceci peut être le résultat d'une option de configuration manquante. Afin de capturer les logs SDK, assurez-vous de sélectionner **Enregistrer les événements utilisateur pour les membres du groupe** dans **Paramètres internes de groupe** pour ce [groupe interne]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/).

### Délai de mise à jour des logs

C'est potentiellement une lenteur normale de la part de notre API.

Lorsque vous appelez les méthodes SDK, le SDK cache généralement ces événements localement et les vide sur le serveur toutes les 10 secondes. Cela peut prendre n'importe où d'une seconde à quelques minutes pour que notre file d'attente de traitement des tâches soit intégrée aux événements les plus récents en fonction de la charge globale à l'époque.

Si vous cherchez des événements pour arriver le plus rapidement possible, essayez d'appeler la fonction `requestImmediateDataFlush()`.

### La fin de la session et le démarrage de la session ont des horodatages similaires (iOS)

Le journal des utilisateurs d'événements montre l'horodatage de la date à laquelle Braze a été informé de la fin de la session, qui sera millisecondes avant le début de la prochaine session. Braze est incapable de savoir que la session s'est terminée avant que l'application ne soit rouverte, car iOS est agressif à propos de l'arrêt de l'exécution des threads lorsque l'application est en arrière-plan, donc aucune donnée ne peut être vidée à Braze jusqu'à ce que l'application soit rouverte.

Alors que l'heure de fin de la session sera spécifiée en secondes avant le début de la session, lorsque l'événement est vidé, la durée de la session est vidée séparément et est correcte, reflétant le moment où l'application a été ouverte. Par conséquent, ce comportement n'affecte pas le filtre `Durée de session médiane`.

En ce qui concerne les sessions utilisateur, vous pouvez utiliser Braze pour surveiller les données telles que:

- Combien de sessions un utilisateur a eu
- Quand un utilisateur a démarré une session pour la dernière fois
- Si l'utilisateur démarre une session après avoir reçu une campagne
- La durée de la session médiane de l'utilisateur

Aucun des éléments ci-dessus n'est affecté par la suppression de l'événement de fin de session lors de la prochaine session.
[10]: {% image_buster /assets/img_archive/rawlogs.png %}
