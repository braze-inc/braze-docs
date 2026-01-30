---
nav_title: Sessions de suivi
article_title: Suivre les sessions via le SDK de Braze
page_order: 3.3
description: "Apprenez à suivre les sessions à l'aide du SDK de Braze."

---

# Sessions de suivi

> Apprenez à suivre les sessions à l'aide du SDK de Braze.

{% alert note %}
Pour les SDK wrapper non répertoriés, utilisez plutôt la méthode native Android ou Swift correspondante.
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## S’abonner aux mises à jour de session

### Étape 1 : S'abonner aux mises à jour

Pour s'abonner aux mises à jour de la session, utilisez la méthode `subscribeToSessionUpdates()`.

{% tabs %}
{% tab web %}
Pour l'instant, s'abonner aux mises à jour de session n'est pas pris en charge pour le SDK Web Braze.
{% endtab %}

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
Si vous enregistrez un rappel de fin de session, il se déclenche lorsque l'application revient au premier plan. La durée de la session est mesurée entre le moment où l'application s'ouvre (en avant-plan) et le moment où elle se ferme (en arrière-plan).

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
{% endtabs %}

### Étape 2 : Suivi de la session de test (optionnel)

Pour tester le suivi des sessions, démarrez une session sur votre appareil, puis ouvrez le tableau de bord de Braze et recherchez l'utilisateur concerné. Dans son profil utilisateur, sélectionnez **Aperçu des sessions.** Si les indicateurs se mettent à jour comme prévu, le suivi de session fonctionne correctement.

![La section d'aperçu des sessions d'un profil utilisateur indique le nombre de sessions, la date de la dernière utilisation et la date de la première utilisation.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
Les détails spécifiques aux applications ne sont affichés que pour les utilisateurs qui ont utilisé plus d'une application.
{% endalert %}

## Modifier le délai de session par défaut {#change-session-timeout}

Vous pouvez modifier le délai qui s'écoule avant qu'une session ne se termine automatiquement.

{% tabs %}
{% tab web %}
Par défaut, le délai d'expiration de la session est fixé à `30` minutes. Pour changer cela, passez l'option `sessionTimeoutInSeconds` à votre fonction [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) fonction. Il peut être défini comme tout nombre entier supérieur ou égal à `1`. 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

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
{% endtabs %}

{% alert note %}
Si vous définissez un délai de session, toute la sémantique de la session s'étendra automatiquement jusqu'au délai défini.
{% endalert %}
