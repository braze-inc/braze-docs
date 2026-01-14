### Messages in-app Slideup

[`Slideup`]{% if include.platform == "iOS" %}[in_app_message_1]{% elsif include.platform == "Android" %}[in_app_message_2]{% endif %} Les messages in-app sont ainsi nommés parce qu'ils « glissent  depuis le haut ou le bas de l'écran.  Ils recouvrent une petite partie de l’écran et offrent une fonctionnalité de messagerie efficace et non intrusive.

![Exemple de contextuel][in_app_message_9]

### Messages in-app modaux

[`Modal`]{% if include.platform == "iOS" %}[in_app_message_3]{% elsif include.platform == "Android" %}[in_app_message_4]{% endif %} Les messages in-app apparaissent au centre de l'écran et sont encadrés par un panneau translucide. Utiles pour les messages critiques, ils peuvent être pourvus de deux boutons d’action et d’analyse.

![Exemple de fenêtre modale][in_app_message_10]

### Messages in-app complets

[`Full`]{% if include.platform == "iOS" %}[in_app_message_5]{% elsif include.platform == "Android" %}[in_app_message_6]{% endif %} Les messages in-app sont utiles pour maximiser le contenu et l'impact de votre communication avec les utilisateurs.  La moitié supérieure d’un message in-app `full` contient une image, et la moitié inférieure affiche le texte et deux boutons d’action et d’analyse.

![Exemple complet][in_app_message_11]

### Messages in-app HTML complets

[`HTML Full`]{% if include.platform == "iOS" %}[in_app_message_7]{% elsif include.platform == "Android" %}[in_app_message_8]{% endif %} Les messages in-app sont utiles pour créer un contenu utilisateur entièrement personnalisé. Le contenu des messages in-app entièrement en HTML défini par l’utilisateur est affiché dans un {% if include.platform == "iOS" %}`WKWebView`{% elsif include.platform == "Android" %}`WebView`{% endif %} et peut éventuellement contenir d’autres contenus enrichis, tels que des images et des polices, permettant un contrôle total de l’apparence et de la fonctionnalité du message.

 {% if include.platform == "iOS" %}
L’exemple suivant montre la mise en page d’un message in-app HTML complet :

![Exemple HTML5][in_app_message_23]

 {% elsif include.platform == "Android" %}L’exemple suivant montre un message in-app HTML complet de sondage créé par Soundcloud.

![Exemple HTML5][in_app_message_12]
{% endif %}

Le contenu d’un message in-app complet est affiché dans un WKWebView et peut éventuellement contenir d’autres contenus enrichis, comme des images et des polices, permettant un contrôle total de l’apparence et des fonctionnalités du message. **Veuillez noter que nous ne prenons actuellement pas en charge l’affichage de messages in-app HTML personnalisés dans un iFrame sur les plateformes iOS et Android.**

## Livraison de messages in-app

### Messages in-app (déclenchés)

La documentation suivante fait référence au produit Braze `In-App Messaging`, également connu sous le nom de "messages in-app déclenchés", dont la marque est mise en évidence ci-dessous dans le menu déroulant "Créer une campagne" :

![Compositeur de messages in-app][in_app_message_13]

Vous pouvez également consulter la documentation relative à notre produit obsolète [`Original In-App Messaging`][in_app_message_14].

#### Types de déclencheurs

Notre produit de messages in-app vous permet de déclencher un affichage de messages in-app suite à plusieurs types d’événements différents : `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`.  En outre, les déclencheurs `Specific Purchase` et `Custom Event` peuvent contenir des filtres de propriétés robustes.

{% alert note %}
Les messages in-app déclenchés ne fonctionnent qu’avec des événements personnalisés enregistrés via le SDK de Braze. Les messages in-app peuvent être déclenchés via l’API ou les événements API (comme les événements d’achat). Si vous travaillez avec Android, découvrez comment [consigner des événements personnalisés sur Android][in_app_message_24]. Si vous travaillez avec iOS, découvrez comment [consigner des événements personnalisés sur iOS][in_app_message_25].
{% endalert %}

#### Sémantiques de livraison

Tous les messages in-app qu’un utilisateur peut recevoir sont délivrés à l’appareil de l’utilisateur au démarrage de session. Pour plus d'informations sur la sémantique de démarrage de session du SDK, consultez notre [documentation sur le cycle de vie des sessions]{% if include.platform == "iOS" %}[in_app_message_15a]{% elsif include.platform == "Android" %}[in_app_message_15b]{% endif %}. Lors de la livraison, le SDK récupère les ressources de manière à ce qu'elles soient disponibles immédiatement au moment du déclenchement, minimisant ainsi la latence de l'affichage.

Lorsqu’un événement déclencheur comporte plus d’un message in-app éligible associé, seul le message in-app avec la priorité la plus élevée sera livré.

Pour les messages in-app qui s'affichent immédiatement lors de la livraison (comme le démarrage de la session, le clic sur une notification push), il peut y avoir une certaine latence due au fait que les ressources ne sont pas capturées à l’avance.

#### Intervalle de temps minimum entre les déclencheurs

Par défaut, nous appliquons des limites de débit d’une fois toutes les 30 secondes pour les messages in-app afin de garantir une expérience utilisateur de qualité.

{% if include.platform == "iOS" %}Vous pouvez remplacer cette valeur par la clé `ABKMinimumTriggerTimeIntervalKey` à l'intérieur du paramètre `appboyOptions` transmis à `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Définissez `ABKMinimumTriggerTimeIntervalKey` sur la valeur d’entier souhaitée comme durée minimale en secondes entre les messages in-app :

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% elsif include.platform == "Android" %}
Pour remplacer cette valeur, définissez `com_appboy_trigger_action_minimum_time_interval_seconds` dans votre `braze.xml`.

```xml
  <integer name="com_appboy_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endif %}

[in_app_message_1]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html
[in_app_message_2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html
[in_app_message_3]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html
[in_app_message_4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html
[in_app_message_5]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html
[in_app_message_6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html
[in_app_message_7]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html
[in_app_message_8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html
[in_app_message_9]: {% image_buster /assets/img_archive/In-App_Slideup.png %}
[in_app_message_10]: {% image_buster /assets/img_archive/In-App_Modal.png %}
[in_app_message_11]: {% image_buster /assets/img_archive/In-App_Full.png %}
[in_app_message_12]: {% image_buster /assets/img_archive/HTML5.gif %}
[in_app_message_13]: {% image_buster /assets/img_archive/trigger-iam-composer.png %}
[in_app_message_14]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/create/#original-in-app-messages
[in_app_message_15a]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle
[in_app_message_15b]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle
[in_app_message_19]: {{ site.baseurl }}/developer_guide/platform_integration_guides/{{ include.platform }}/in-app_messaging/#in-app-messages-déclenchés
[in_app_message_23]: {% image_buster /assets/img_archive/ios-html-full-iam.gif %}
[in_app_message_24]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events
[in_app_message_25]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events

