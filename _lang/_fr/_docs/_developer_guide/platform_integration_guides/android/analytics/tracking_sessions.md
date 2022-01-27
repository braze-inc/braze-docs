---
nav_title: Sessions de suivi
article_title: Suivi des sessions pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 0
description: "Cet article de référence montre comment s'abonner aux mises à jour de session pour votre application Android."
---

# Suivi de session pour Android/FireOS

Le Braze SDK rapporte les données de session qui sont utilisées par le tableau de bord Braze pour calculer l'engagement des utilisateurs et d'autres analyses intégrales à la compréhension de vos utilisateurs. Basé sur la sémantique de session ci-dessous, notre SDK génère des points de données "démarrer la session" et "fermer la session" qui tiennent compte de la durée de la session et compte des sessions visibles dans le tableau de bord de Braze.

## Cycle de vie de session

Si vous avez intégré Braze en utilisant notre recommandation \[Intégration du cycle de vie de l'activité\] \[session_tracking_8\], `openSession()` et `closeSession()` seront appelées automatiquement pour chaque activité de votre application. Par défaut, les sessions sur Android sont ouvertes lors du premier appel à `openSession()` et sont fermées après qu'une application a été hors de l'avant-plan pendant plus de 10 secondes.  Notez que l'appel à `closeSession()` ne ferme pas une session immédiatement. Plutôt, il ferme une session en 10 secondes si l'utilisateur n'appelle pas `openSession()` (par exemple, en naviguant vers une autre Activité) dans l'intervalle.

Une session Android expire après 10 secondes sans aucune communication de l'application hôte. Cela signifie que si un utilisateur arrière-plan l'application et retourne 9 secondes plus tard, la même session sera poursuivie.

__Remarque :__ Si une session se termine alors que l'utilisateur a l'application en arrière-plan, que les données ne peuvent pas être vidées vers le serveur tant que l'application n'est pas rouverte.

**Note**: Si vous avez besoin de forcer une nouvelle session, vous pouvez le faire en changeant d'utilisateurs.

## Personnalisation du délai d'attente de la session
Pour personnaliser le délai d'attente de la session, ajoutez `com_appboy_session_timeout` à votre fichier [`braze.xml`][session_tracking_3]:

```xml
<!-- La durée de temps avant qu'une session ne se termine en secondes. Le gestionnaire de session "rouvrira" sinon les sessions fermées si l'appel à StartSession intervient dans cet intervalle. (défaut est 10) -->
<integer name="com_appboy_session_timeout">NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT</integer>
```

**Remarque**: La valeur minimale pour `sessionTimeoutInSeconds` est de 1 seconde.

## Tests de suivi de session

Pour détecter les sessions via votre utilisateur, trouvez votre utilisateur sur le tableau de bord et accédez à "Utilisation de l'application" sur le profil de l'utilisateur. Vous pouvez confirmer que le suivi de session fonctionne en vérifiant que la métrique "essions" augmente quand vous vous y attendez.

!\[test_session\] \[session_tracking_7\]

## S'abonner aux mises à jour de la session

Le SDK Braze fournit un abonné [`subscribeToSessionUpdates`][1] pour écouter les mises à jour de la session.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
  @Override
  public void trigger(SessionStateChangedEvent message) {
    if (message. etEventType() == SessionStateChangedEvent.ChangeType. ESSION_STARTED) {
      // Une session vient de commencer
    }
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // Une session vient de commencer
  }
}
```

{% endtab %}
{% endtabs %}
[session_tracking_1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/#customizing-braze-on-startup [session_tracking_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml [session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %} [session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android

[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/subscribe-to-session-updates.html
