---
nav_title: Guide d’implémentation avancée (facultatif)
article_title: Implémentation avancée de notifications push pour Android (facultatif)
platform: Android
page_order: 29
description: "Ce guide d’implémentation avancé explique comment personnaliser la mise en page des notifications push pour afficher des informations spécifiques à l’utilisateur dans vos messages. Il contient également un exemple de cas d’usage créé par notre équipe, les extraits de code l’accompagnant et des directives concernant l’enregistrement des analyses."
channel:
  - push
---

<br>
{% alert important %}
Vous recherchez le guide d’intégration de base du développeur de notifications push ? Trouvez-le [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/).
{% endalert %}

# Guide d’implémentation avancé

> Ce guide d’implémentation en option et avancé couvre les moyens d’exploiter une sous-classe personnalisée FirebaseMessagingService pour tirer le meilleur parti de vos messages de notification push. Il contient également un cas d’usage personnalisé créé par notre équipe, les extraits de code l’accompagnant et des directives concernant l’enregistrement des analyses. Visitez notre dépôt de démonstrations Braze [ici](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Notez que ce guide d’implémentation est centré autour d’une implémentation Kotlin, mais les extraits de code Java sont fournis aux personnes intéressées.

## Disposition personnalisée des notifications

Les notifications de Braze sont envoyées sous forme de [messages de données](https://firebase.google.com/docs/cloud-messaging/concept-options), ce qui signifie que votre application aura toujours une chance de répondre et d'effectuer un comportement en conséquence, même en arrière-plan (contrairement aux messages de notification, qui peuvent être traités automatiquement par le système lorsque votre application est en arrière-plan). Ainsi, votre application aura la possibilité de personnaliser l’expérience, par exemple en affichant des éléments d’IU personnalisés dans la notification envoyée à la barre de notification. Bien que l'implémentation de push de cette manière puisse être peu familière à certains, l'une de nos fonctionnalités bien connues chez Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), est un excellent exemple de l'utilisation de composants de vue personnalisés pour créer une expérience engageante !

#### Conditions

Android impose certaines limitations sur les composants pouvant être utilisés pour implémenter des vues personnalisées. Les dispositions de la vue de la notification doivent _uniquement_ contenir des objets de vue compatibles avec le framework [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews).

### Notifications push personnalisées

Les notifications push peuvent afficher des informations spécifiques à l’utilisateur dans une hiérarchie de vue personnalisée. L’exemple suivant montre une notification push après qu’un utilisateur a terminé une tâche spécifique (Cours d'apprentissage de Braze) et est maintenant encouragé à développer cette notification pour vérifier son progrès. Les informations fournies ici sont spécifiques à l’utilisateur et peuvent être lancées à la fin de la session ou après une action spécifique de l’utilisateur en tirant parti d’un déclencheur API. 

![Exemple de tableau de bord personnalisé]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

#### Configuration du tableau de bord

Pour mettre en place un push personnalisé dans le tableau de bord, vous devez enregistrer la catégorie spécifique que vous souhaitez voir s'afficher. Définissez les attributs utilisateur appropriés que vous souhaitez voir apparaître dans le message au sein des paires clé-valeur à l'aide de Liquid standard. Ces vues peuvent être personnalisées sur la base des attributs utilisateur spécifiques d’un profil utilisateur donné.

![Exemple de tableau de bord personnalisé]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

##### Prêt à enregistrer l’analyse ?
Consultez la [section suivante](#logging-analytics) pour mieux comprendre à quoi doit ressembler le flux de données.

## Enregistrer les analyses

### Enregistrer avec l’API Braze (recommandé)

L'enregistrement des analyses peut uniquement se faire en temps réel avec l'aide du serveur du client qui utilise notre endpoint [`/users/track`.]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Pour enregistrer l’analyse, envoyez la valeur `braze_id` dans le champ des paires clé-valeur (comme indiqué dans la capture d’écran suivante) pour identifier le profil utilisateur à mettre à jour.

![Exemple de tableau de bord personnalisé]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:80%;"}

### Enregistrement manuel 

Vous pouvez enregistrer manuellement en enregistrant les éléments que vous souhaitez soit dans votre implémentation `FirebaseMessagingService.onMessageReceived` soit dans votre activité de démarrage, en fonction des compléments présents dans la charge utile. Cependant, il est important de se rappeler que votre sous-classe `FirebaseMessagingService` _doit_ terminer son exécution dans les 10 secondes suivant l'invocation afin d'éviter d'être [signalée ou interrompue](https://firebase.google.com/docs/cloud-messaging/android/receive) par le système Android. 


