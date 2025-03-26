---
nav_title: Session Tracking
article_title: Session Tracking für iOS
platform: Swift
page_order: 0
search_rank: 1
description: "Dieser Referenzartikel zeigt, wie Sie Updates für das Swift SDK abonnieren können."

---

# Session-Tracking

> Das Braze SDK meldet Sitzungsdaten, die vom Braze Dashboard verwendet werden, um das Nutzer-Engagement und andere Analysen zu berechnen, die für das Verständnis Ihrer Nutzer:innen wichtig sind. 

Unser SDK generiert Datenpunkte für "Sitzung starten" und "Sitzung schließen", die die Sitzungslänge und die Anzahl der Sitzungen berücksichtigen und im Braze-Dashboard auf der Grundlage der folgenden Session-Semantik angezeigt werden können.

## Lebenszyklus einer Sitzung

Eine Sitzung wird gestartet, wenn Sie `Braze.init(configuration:)` aufrufen. Standardmäßig geschieht dies, wenn die Benachrichtigung `UIApplicationWillEnterForegroundNotification` ausgelöst wird (wenn die App in den Vordergrund tritt). Das Sitzungsende tritt ein, wenn die App den Vordergrund verlässt (z. B. wenn die Benachrichtigung `UIApplicationDidEnterBackgroundNotification` ausgelöst wird oder wenn die App beendet wird).

{% alert note %}
Wenn Sie eine neue Sitzung erzwingen müssen, können Sie dies tun, indem Sie den Nutzer wechseln.
{% endalert %}

## Anpassen des Sitzungs-Timeouts

Sie können den `sessionTimeout` auf den gewünschten Integer-Wert in Ihrem `configuration`-Objekt setzen, das an [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class) übergeben wird.

{% tabs %}
{% tab schnell %}

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
{% tab objektiv-c %}

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

Wenn Sie einen Timeout für die Sitzung festgelegt haben, erstreckt sich die Session-Semantik auf diesen angepassten Timeout.

{% alert note %}
Der Mindestwert für `sessionTimeout` ist 1 Sekunde. Der Standardwert ist 10 Sekunden.
{% endalert %}

## Testen des Sitzungs-Trackings

Um Sitzungen über Ihren Nutzer:innen zu erkennen, suchen Sie Ihren Nutzer auf dem Dashboard und navigieren Sie auf dem Nutzerprofil zur **Übersicht der Sitzungen**. Um sicherzugehen, dass das Sitzungs-Tracking funktioniert, können Sie überprüfen, ob die Metrik "Sitzungen" ansteigt, wenn Sie es erwarten. App-spezifische Details werden angezeigt, wenn der Nutzer mehr als eine App verwendet hat.

![Die Übersicht über die Sitzungen eines Nutzerprofils, die die Anzahl der Sitzungen, das Datum der letzten Nutzung und das Datum der ersten Nutzung anzeigt.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:40%;"}

App-spezifische Details werden nur angezeigt, wenn der Nutzer mehr als eine App verwendet hat.

## Updates für Sitzungen abonnieren

Um auf Updates von Sitzungen zu prüfen, verwenden Sie die Methode [`subscribeToSessionUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/subscribetosessionupdates(_:)). Ereignisse zu Beginn und Ende einer Sitzung werden nur protokolliert, wenn die App im Vordergrund läuft. Wenn Sie einen Callback für Sitzungsende-Ereignisse registrieren und die App im Hintergrund läuft, wird der Callback ausgelöst, wenn die App wieder in den Vordergrund kommt. Die Sitzungsdauer wird jedoch nach wie vor als die Zeit von der Öffnung oder dem Foregrounding der App bis zu ihrem Schließen oder Backgrounding gemessen.

{% tabs %}
{% tab schnell %}
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

{% tab objektiv-c %}
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

Alternativ dazu können Sie in Swift die Funktion [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) `AsyncStream` verwenden, um asynchrone Änderungen zu beobachten:

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

