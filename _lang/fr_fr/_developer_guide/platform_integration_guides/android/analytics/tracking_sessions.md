---
nav_title: Suivre des sessions
article_title: Suivre des sessions pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 0
description: "Cet article de référence montre comment vous abonner aux mises à jour de session pour votre application Android ou FireOS."

---

# Suivre des sessions

> Le SDK Braze rapporte les données de session utilisées par le tableau de bord de Braze pour calculer l’engagement des utilisateurs et d’autres analyses essentielles à une meilleure connaissance de vos utilisateurs. Sur la base de la sémantique de session suivante, notre SDK génère des points de données « démarrage de la session » et « fin de la session » qui comptent pour la longueur de session et le nombre de sessions visibles dans le tableau de bord de Braze. Cet article de référence montre comment vous abonner aux mises à jour de session pour votre application Android ou FireOS.

## Cycle de vie de la session

Si vous avez intégré Braze à l'aide de notre intégration recommandée [activity lifecycle callback integration]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android), `openSession()` et `closeSession()` seront appelés automatiquement pour chaque activité dans votre application. Par défaut, les sessions sur Android sont ouvertes dès le premier appel vers `openSession()` et sont fermées après que l’application a été hors du premier plan pendant plus de 10 secondes. Notez qu’appeler `closeSession()` ne ferme pas une session immédiatement. Plutôt, cela ferme une session en 10 secondes si l'utilisateur n'appelle pas `openSession()` (par exemple, en naviguant vers une autre activité) entre-temps.

Une session Android expire après 10 secondes sans aucune communication de l’application hôte. Cela signifie que si un utilisateur passe l’application en arrière-plan et y retourne 9 secondes plus tard, la même session sera poursuivie. Notez que si une session se ferme alors que l'utilisateur a l'application en arrière-plan, ces données peuvent ne pas être envoyées au serveur jusqu'à ce que l'application soit rouverte.

{% alert note %}
Si vous devez forcer une nouvelle session, vous pouvez le faire en changeant d’utilisateur.
{% endalert %}

## Personnaliser la libération sur temporisation de session
Pour personnaliser le délai d'attente de la session, ajoutez `com_braze_session_timeout` à votre fichier [`braze.xml`]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-brazexml). La valeur minimale pour `NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT` est de 1 seconde.

```xml
<!-- The length of time before a session times out in seconds. The session manager will "re-open" otherwise closed sessions if the call to StartSession comes within this interval. (default is 10) -->
<integer name="com_braze_session_timeout">NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT</integer>
```

## Tester le suivi de session

Pour détecter les sessions via votre utilisateur, trouvez votre utilisateur sur le tableau de bord et accédez à **Utilisation de l'application** sur le profil de l'utilisateur. Vous pouvez confirmer que le suivi de session fonctionne en vérifiant que la métrique de session augmente lorsque vous vous y attendez.

![Un profil utilisateur indiquant le nombre de sessions, la date de la première et de la dernière utilisation de l'application.]({% image_buster /assets/img_archive/test_session.png %})

## S’abonner aux mises à jour de session

Le SDK Braze fournit une fonction d’abonnement [`subscribeToSessionUpdates`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-session-updates.html) pour écouter les mises à jour de session :

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

