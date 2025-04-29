{% multi_lang_include developer_guide/prerequisites/android.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Disposition personnalisée des notifications

Les notifications de Braze sont envoyées sous forme de [messages de données](https://firebase.google.com/docs/cloud-messaging/concept-options), ce qui signifie que votre application aura toujours une chance de répondre et d'effectuer un comportement en conséquence, même en arrière-plan (contrairement aux messages de notification, qui peuvent être traités automatiquement par le système lorsque votre application est en arrière-plan). Ainsi, votre application aura la possibilité de personnaliser l’expérience, par exemple en affichant des éléments d’IU personnalisés dans la notification envoyée à la barre de notification. Bien que l'implémentation de push de cette manière puisse être peu familière à certains, l'une de nos fonctionnalités bien connues chez Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), est un excellent exemple de l'utilisation de composants de vue personnalisés pour créer une expérience engageante !

{% alert important %}
Android impose certaines limitations sur les composants pouvant être utilisés pour implémenter des vues personnalisées. Les dispositions de la vue de la notification doivent _uniquement_ contenir des objets de vue compatibles avec le framework [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews).
{% endalert %}

## Notifications push personnalisées

Les notifications push peuvent afficher des informations spécifiques à l’utilisateur dans une hiérarchie de vue personnalisée. Dans l'exemple suivant, un déclencheur API est utilisé pour envoyer une notification push personnalisée à un utilisateur afin qu'il puisse suivre sa progression après avoir effectué une tâche spécifique dans l'application.

![Exemple de tableau de bord personnalisé]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

Pour configurer un push personnalisé dans le tableau de bord, enregistrez la catégorie spécifique que vous souhaitez voir s'afficher, puis définissez tous les attributs utilisateur pertinents que vous souhaitez afficher à l'aide de Liquid.

![Exemple de tableau de bord personnalisé]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}
