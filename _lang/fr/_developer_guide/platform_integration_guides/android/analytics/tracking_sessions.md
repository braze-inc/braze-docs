---
nav_title: Suivre des sessions
article_title: Suivre des sessions pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 0
description: "Cet article de référence montre comment vous abonner aux mises à jour de session pour votre application Android ou FireOS."

---

# Suivre une session pour Android et FireOS

Le SDK Braze rapporte les données de session utilisées par le tableau de bord de Braze pour calculer l’engagement des utilisateurs et d’autres analytiques essentielles à la compréhension de vos utilisateurs. Sur la base de la sémantique de session suivante, notre SDK génère des points de données « démarrage de la session » et « fin de la session » qui comptent pour la longueur de session et le nombre de sessions visibles dans le tableau de bord de Braze.

## Cycle de vie de la session

Si vous avez intégré Braze à l’aide de l’[intégration de la fonction de rappel du cycle de vie de l’activité][session_tracking_8], ce que nous recommandons, `openSession()` et `closeSession()` seront appelés automatiquement pour chaque activité de votre application. Par défaut, les sessions sur Android sont ouvertes dès le premier appel vers `openSession()` et sont fermées après que l’application a été hors du premier plan pendant plus de 10 secondes. Notez qu’appeler `closeSession()` ne ferme pas une session immédiatement. Il ferme plutôt une session en 10 secondes si l’utilisateur n’appelle pas `openSession()` (par exemple, en naviguant vers une autre activité) pendant ce temps.

Une session Android expire après 10 secondes sans aucune communication de l’application hôte. Cela signifie que si un utilisateur passe l’application en arrière-plan et y retourne 9 secondes plus tard, la même session sera poursuivie. Notez que si une session se ferme alors que l’utilisateur a mis l’application en arrière-plan, les données peuvent ne pas s’effacer du serveur avant l’ouverture suivante de l’application.

{% alert note %}
Si vous devez forcer une nouvelle session, vous pouvez le faire en changeant d’utilisateur.
{% endalert %}

## Personnaliser la libération sur temporisation de session
Pour personnaliser la libération sur temporisation de session, ajoutez `com_braze_session_timeout` à votre fichier [`braze.xml`][session_tracking_3]. La valeur minimale pour `NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT` est de 1 seconde.

```xml
<!-- The length of time before a session times out in seconds. The session manager will "re-open" otherwise closed sessions if the call to StartSession comes within this interval. (default is 10) -->
<integer name="com_braze_session_timeout">NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT</integer>
```

## Tester le suivi de session

Pour détecter les sessions à l’aide de votre utilisateur, recherchez-le sur le tableau de bord et naviguez jusqu’à **Utilisation de l’application** dans le profil utilisateur. Vous pouvez confirmer que le suivi de session fonctionne en vérifiant que la métrique de session augmente lorsque vous vous y attendez.

![Un composant de profil utilisateur indiquant le nombre de sessions survenues, quand l’application a été utilisée pour la première fois et pour la dernière fois.][session_tracking_7]

## S’abonner aux mises à jour de session

Le SDK Braze fournit une fonction d’abonnement [`subscribeToSessionUpdates`][1] pour écouter les mises à jour de session :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
  @Override
  public void trigger(SessionStateChangedEvent message) {
    if (message.getEventType() == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
      // A session has just been started
    }
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endtab %}
{% endtabs %}

[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-session-updates.html
[session_tracking_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-brazexml
[session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %}
[session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android
