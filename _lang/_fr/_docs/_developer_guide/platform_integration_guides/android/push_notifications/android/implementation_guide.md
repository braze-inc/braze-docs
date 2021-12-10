---
nav_title: Implémentation avancée (facultatif)
article_title: Implémentation avancée des notifications Push pour Android (facultatif)
platform: Android
page_order: 29
description: "Ce guide de mise en œuvre avancé couvre la façon de personnaliser la mise en page des notifications push pour afficher des informations spécifiques à l'utilisateur dans vos messages. On y trouve également un exemple de cas d'utilisation construit par notre équipe, des extraits de code accompagnateurs et des conseils sur la journalisation des analyses."
channel:
  - Pousser
---

<br>
{% alert important %}
Vous recherchez le guide d'intégration des développeurs Push ? Trouvez-le [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/).
{% endalert %}

# Guide d'implémentation des notifications push

> Ce guide d'implémentation optionnel et avancé couvre les moyens de tirer parti d'une sous-classe FirebaseMessagingService personnalisée pour tirer le meilleur parti de vos messages push. Included is a custom use case built by our team, accompanying code snippets, and guidance on logging analytics. Visitez notre Dépôt de Démo de Braze [ici](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Veuillez noter que ce guide d'implémentation est centré sur une implémentation de Kotlin, mais des extraits de code Java sont fournis pour ceux qui sont intéressés.

## Disposition de notification personnalisée

Les notifications Braze sont envoyées sous la forme de [messages de données](https://firebase.google.com/docs/cloud-messaging/concept-options), ce qui signifie que votre application aura toujours une chance de répondre et d'exécuter des comportements en conséquence, même en arrière-plan (c'est en contraste avec les messages de notification, qui peuvent être gérées automatiquement par le système lorsque votre application est en arrière-plan). Ainsi, votre application aura une chance de personnaliser l'expérience par, par exemple en affichant des éléments personnalisés de l'interface utilisateur dans la barre de notification délivrée dans la zone de notification. Alors que l'implémentation de la poussée de cette manière peut ne pas être familière à certains, l'une de nos caractéristiques bien connues au Brésil, [Les Histoires Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), sont un excellent exemple d'utilisation de composants de vue personnalisés pour créer une expérience engageante !

#### Exigences

Android impose certaines limitations sur quels composants peuvent être utilisés pour implémenter des vues de notification personnalisées. Les mises en page de la vue de notification doivent _seulement_ contenir des objets de vue compatibles avec le framework [Vues à distance](https://developer.android.com/reference/android/widget/RemoteViews).

### Notifications push personnalisées

Les notifications push peuvent afficher des informations spécifiques à l'utilisateur dans une hiérarchie de vue personnalisée. L'exemple ci-dessous montre une notification push après qu'un utilisateur a terminé une tâche spécifique (Braze LAB cours) et est maintenant encouragé à étendre cette notification pour vérifier leur progression. Les informations fournies ici sont spécifiques à l'utilisateur et peuvent être désactivées au moment où une session est terminée ou une action spécifique de l'utilisateur est prise en utilisant un déclencheur d'API.

!\[Exemple de tableau de bord Push personnalisé\]\[1\]{: style="max-width:65%;border:0"}

#### Configuration du tableau de bord

Pour configurer un push personnalisé dans le tableau de bord, vous devez enregistrer la catégorie spécifique que vous souhaitez afficher. Définissez les attributs utilisateur appropriés que vous souhaitez afficher dans les paires clé-valeur en utilisant Liquid standard. Ces vues peuvent être personnalisées en fonction des attributs spécifiques d'un utilisateur d'un profil utilisateur spécifique.

!\[Exemple de tableau de bord Push personnalisé\]\[2\]{: style="max-width:60%;"}

##### Prêt à enregistrer des analyses ?
Visitez la section [suivante](#logging-analytics) pour mieux comprendre à quoi devrait ressembler le flux de données.

## Analyses de la journalisation

### Journalisation avec l'API Braze (recommandé)

L'analyse de journalisation ne peut être effectuée en temps réel qu'avec l'aide du serveur du client qui touche l'API [utilisateurs/suivi]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) du point de terminaison de l'API de Braze. Pour enregistrer les analyses, envoyer vers le bas la valeur `braze_id` dans le champ des paires clé-valeur (comme vu dans la capture d'écran ci-dessous) pour identifier quel profil utilisateur mettre à jour.

!\[Exemple de tableau de bord Push personnalisé\]\[3\]{: style="max-width:80%;"}

### Logs manuellement

La journalisation manuelle peut être effectuée en enregistrant les éléments que vous souhaitez dans votre `FirebaseMessagingService . nMessageReceived` implémentation ou depuis votre activité de démarrage, basé sur les extras présents dans la charge utile. Cependant, une mise en garde importante à se rappeler est que votre sous-classe `FirebaseMessagingService` _doit_ terminer l'exécution dans les 10 secondes suivant l'invocation pour éviter d'être [signalé ou résilié](https://firebase.google.com/docs/cloud-messaging/android/receive) par le système Android.
[1]: {% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %} [2]: {% image_buster /assets/img/push_implementation_guide/push5.png %} [3]: {% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}
