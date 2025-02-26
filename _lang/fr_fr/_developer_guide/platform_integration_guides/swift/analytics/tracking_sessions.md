---
nav_title: Suivi des sessions
article_title: Suivi de session pour iOS
platform: Swift
page_order: 0
search_rank: 1
description: "Cet article de référence montre comment s'abonner aux mises à jour de sessions pour le SDK Swift."

---

# Suivi d’une session

> Le SDK Braze rapporte les données de session utilisées par le tableau de bord de Braze pour calculer l’engagement des utilisateurs et d’autres analyses essentielles à une meilleure connaissance de vos utilisateurs. 

Notre SDK génère des points de données « démarrage de session » et « fin de session » qui comptent pour la longueur de session et le comptage de sessions visibles dans le tableau de bord de Braze en fonction des sémantiques de session suivantes.

## Cycle de vie de la session

Une session est lancée lorsque vous appelez `Braze.init(configuration:)`. Par défaut, cela se produit lorsque la notification `UIApplicationWillEnterForegroundNotification` est déclenchée (lorsque l'application passe au premier plan). La fin de la session survient lorsque l'application quitte le premier plan (par exemple lorsque la notification `UIApplicationDidEnterBackgroundNotification` est déclenchée ou lorsque l'application meurt).

{% alert note %}
Si vous devez forcer une nouvelle session, vous pouvez le faire en changeant d’utilisateur.
{% endalert %}

## Personnaliser la libération sur temporisation de session

Vous pouvez fixer la valeur de `sessionTimeout` à la valeur entière souhaitée dans votre objet `configuration` transmis à [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class).

{% tabs %}
{% tab swift %}

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
{% endtab %}
{% tab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

Si vous avez défini un délai de libération sur temporisation de session, les sémantiques de session s’étendent à toute cette temporisation personnalisée.

{% alert note %}
La valeur minimale pour `sessionTimeout` est de 1 seconde. La valeur par défaut est 10 secondes.
{% endalert %}

## Tester le suivi de session

Pour détecter les sessions via votre utilisateur, trouvez votre utilisateur sur le tableau de bord et naviguez vers **Aperçu des sessions** sur le profil de l'utilisateur. Vous pouvez confirmer que le suivi de session fonctionne en vérifiant que la métrique « session » augmente lorsque vous vous y attendez. Les détails spécifiques aux applications s'affichent lorsque l'utilisateur a utilisé plus d'une application.

![Section d'aperçu des sessions d'un profil utilisateur indiquant le nombre de sessions, la date de la dernière utilisation et la date de la première utilisation.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:40%;"}

Les détails spécifiques aux applications ne s'affichent que si l'utilisateur a utilisé plus d'une application.

## S’abonner aux mises à jour de session

Pour écouter les mises à jour de session, utilisez la méthode [`subscribeToSessionUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/subscribetosessionupdates(_:)). Les événements de début et de fin de session ne sont enregistrés que lorsque l'application fonctionne au premier plan. Si vous enregistrez un rappel pour les événements de fin de session et que l'application est en arrière-plan, le rappel se déclenchera lorsque l'application sera à nouveau en avant-plan. Toutefois, la durée de la session est toujours mesurée comme le temps écoulé entre l'ouverture de l'application ou le passage en avant-plan et la fermeture de l'application ou le passage en arrière-plan.

{% tabs %}
{% tab swift %}
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
{% endtab %}

{% tab objective-c %}
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
{% endtab %}
{% endtabs %}

Dans Swift, vous pouvez également utiliser le `AsyncStream` [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) pour observer les changements asynchrones :

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

