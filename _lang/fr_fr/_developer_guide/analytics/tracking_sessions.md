---
nav_title: Suivre des sessions
article_title: Suivi des sessions via le SDK de Braze
page_order: 3.3
description: "Apprenez à suivre les sessions à l'aide du SDK de Braze."

---

# Sessions de suivi

> Apprenez à suivre les sessions à l'aide du SDK de Braze.

{% alert note %}
Pour les SDK wrapper non répertoriés, utilisez plutôt la méthode native Android ou Swift correspondante.
{% endalert %}

## À propos du cycle de vie de la session

Une session désigne la période pendant laquelle le SDK de Braze suit l'activité de l'utilisateur dans votre application après son lancement. Vous pouvez également forcer une nouvelle session en [appelant la méthode `changeUser()` ]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).

{% tabs %}
{% tab android %}
{% alert note %}
Si vous avez configuré le [rappel du cycle de vie de l'activité]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) pour Android, Braze appellera automatiquement `openSession()` et `closeSession()` pour chaque activité de votre application.
{% endalert %}

Par défaut, une session démarre lorsque `openSession()` est appelé pour la première fois. Si votre application passe en arrière-plan, la session restera active pendant `10` secondes (sauf si vous [modifiez le délai d'attente par défaut](#changing-the-default-session-timeout)) ou si l'utilisateur ferme votre application. Gardez à l'esprit que si l'utilisateur ferme votre application alors qu'elle est en arrière-plan, les données de session peuvent ne pas être définies dans Braze jusqu'à ce qu'il rouvre l'application. 

L'appel à `closeSession()` ne met pas immédiatement fin à la session. Au lieu de cela, il mettra fin à la session au bout de 10 secondes si `openSession()` n'est pas appelé à nouveau par l'utilisateur qui démarre une autre activité.
{% endtab %}

{% tab swift %}
Par défaut, une session démarre lorsque vous appelez `Braze.init(configuration:)`. Cela se produit lorsque la notification `UIApplicationWillEnterForegroundNotification` est déclenchée, ce qui signifie que l'application est passée au premier plan.

Si votre application passe en arrière-plan, `UIApplicationDidEnterBackgroundNotification` sera déclenché. La session restera active pendant `10` secondes (sauf si vous [modifiez le délai d'attente par défaut](#changing-the-default-session-timeout)) ou si l'utilisateur ferme votre application.
{% endtab %}

{% tab web %}
Par défaut, une session démarre lorsque vous appelez `braze.openSession()` pour la première fois. La session restera active jusqu'à `30` minutes d'inactivité (sauf si vous [modifiez le délai d'attente par défaut](#change-session-timeout)) ou si l'utilisateur ferme l'application.
{% endtab %}
{% endtabs %}

## S’abonner aux mises à jour de session

### Étape 1 : S'abonner aux mises à jour

Pour s'abonner aux mises à jour de la session, utilisez la méthode `subscribeToSessionUpdates()`.

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab java %}

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

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
Si vous enregistrez un rappel de fin de session, il se déclenche lorsque l'application revient au premier plan. La durée de la session est mesurée entre le moment où l'application s'ouvre (avant-plan) et le moment où elle se ferme (arrière-plan).

{% subtabs %}
{% subtab swift %}
```swift
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.subscribeToSessionUpdates { event in
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```

Pour s'abonner à un flux asynchrone, vous pouvez utiliser [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) à la place.

```swift
for await event in braze.sessionUpdatesStream {
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```
{% endsubtab %}

{% subtab objective-c %}
```objc
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
BRZCancellable *cancellable = [AppDelegate.braze subscribeToSessionUpdates:^(BRZSessionEvent * _Nonnull event) {
  switch (event.state) {
    case BRZSessionStateStarted:
      NSLog(@"Session %@ has started", event.sessionId);
      break;
    case BRZSessionStateEnded:
      NSLog(@"Session %@ has ended", event.sessionId);
      break;
    default:
      break;
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
Pour l'instant, s'abonner aux mises à jour de session n'est pas pris en charge pour le SDK de Braze Web.
{% endtab %}
{% endtabs %}

### Étape 2 : Suivi de la session de test (optionnel)

Pour tester le suivi des sessions, démarrez une session sur votre appareil, puis ouvrez le tableau de bord de Braze et recherchez l'utilisateur concerné. Dans son profil utilisateur, sélectionnez **Aperçu des sessions.** Si les indicateurs se mettent à jour comme prévu, le suivi de session fonctionne correctement.

![Section d'aperçu des sessions d'un profil utilisateur indiquant le nombre de sessions, la date de la dernière utilisation et la date de la première utilisation.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
Les détails spécifiques aux applications ne sont affichés que pour les utilisateurs qui ont utilisé plus d'une application.
{% endalert %}

## Modifier le délai de session par défaut {#change-session-timeout}

Vous pouvez modifier le délai qui s'écoule avant qu'une session ne se termine automatiquement.

{% tabs %}
{% tab android %}
Par défaut, le délai d'attente de la session est fixé à `10` secondes. Pour modifier cela, ouvrez votre fichier `braze.xml` et ajoutez le paramètre `com_braze_session_timeout`. Il peut être défini comme tout nombre entier supérieur ou égal à `1`.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
Par défaut, le délai d'attente de la session est fixé à `10` secondes. Pour modifier cela, définissez `sessionTimeout` dans l'objet `configuration` qui est transmis à [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class). Il peut être défini comme tout nombre entier supérieur ou égal à `1`.

{% subtabs %}
{% subtab swift %}
```swift
// Sets the session timeout to 60 seconds
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.sessionTimeout = 60;
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endsubtab %}
{% subtab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
Par défaut, le délai d'attente de la session est fixé à `30` secondes. Pour changer cela, passez l'option `sessionTimeoutInSeconds` à votre fonction [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) fonction. Il peut être défini comme tout nombre entier supérieur ou égal à `1`. 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}
{% endtabs %}

{% alert note %}
Si vous définissez un délai de session, toute la sémantique de la session s'étendra automatiquement jusqu'au délai défini.
{% endalert %}
