---
nav_title: Tracken von Sitzungen
article_title: Tracking von Sitzungen über das Braze SDK
page_order: 3.3
description: "Erfahren Sie, wie Sie Sitzungen über das Braze SDK tracken können."

---

# Tracking von Sitzungen

> Erfahren Sie, wie Sie Sitzungen über das Braze SDK tracken können.

{% alert note %}
Für Wrapper-SDKs, die nicht aufgeführt sind, verwenden Sie stattdessen die entsprechende native Android- oder Swift-Methode.
{% endalert %}

## Über den Lebenszyklus einer Sitzung

Eine Sitzung referenziert den Zeitraum, in dem das Braze SDK die Aktivitäten der Nutzer:in Ihrer App nach deren Start verfolgt. Sie können auch eine neue Sitzung erzwingen, indem [Sie die Methode `changeUser()` aufrufen]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).

{% tabs %}
{% tab android %}
{% alert note %}
Wenn Sie den [activity lifecycle callback]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) für Android eingerichtet haben, wird Braze automatisch `openSession()` und `closeSession()` für jede Aktivität in Ihrer App aufrufen.
{% endalert %}

Standardmäßig wird eine Sitzung gestartet, wenn `openSession()` zum ersten Mal aufgerufen wird. Wenn Ihre App in den Hintergrund geht, bleibt die Sitzung für `10` Sekunden aktiv (es sei denn, Sie [ändern den Standard-Timeout für die Sitzung](#changing-the-default-session-timeout)) oder der Nutzer:innen schließt Ihre App. Denken Sie daran: Wenn der Nutzer:in Ihre App schließt, während diese im Hintergrund läuft, werden die Sitzungsdaten möglicherweise erst dann in Braze gespeichert, wenn er die App erneut öffnet. 

Wenn Sie `closeSession()` aufrufen, wird die Sitzung nicht sofort beendet. Stattdessen wird die Sitzung nach 10 Sekunden beendet, wenn `openSession()` nicht erneut vom Nutzer:innen aufgerufen wird, der eine andere Aktivität startet.
{% endtab %}

{% tab schnell %}
Standardmäßig beginnt eine Sitzung, wenn Sie `Braze.init(configuration:)` aufrufen. Dies geschieht, wenn die Benachrichtigung `UIApplicationWillEnterForegroundNotification` getriggert wird, was bedeutet, dass die App in den Vordergrund getreten ist.

Wenn Ihre App in den Hintergrund geht, wird `UIApplicationDidEnterBackgroundNotification` getriggert. Die Sitzung bleibt für `10` Sekunden aktiv (es sei denn, Sie [ändern den Standard-Timeout für die Sitzung](#changing-the-default-session-timeout)) oder der Nutzer:innen schließt Ihre App.
{% endtab %}

{% tab Internet %}
Standardmäßig beginnt eine Sitzung, wenn Sie `braze.openSession()` zum ersten Mal aufrufen. Die Sitzung bleibt bis zu `30` Minuten der Inaktivität aktiv (es sei denn, Sie [ändern den Standard-Timeout für die Sitzung](#change-session-timeout)) oder der Nutzer:innen schließt die App.
{% endtab %}
{% endtabs %}

## Updates für Sitzungen abonnieren

### Schritt 1: Updates abonnieren

Um Updates für Sitzungen zu abonnieren, verwenden Sie die Methode `subscribeToSessionUpdates()`.

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

{% tab schnell %}
Wenn Sie einen Callback für das Sitzungsende registrieren, wird dieser ausgelöst, wenn die App in den Vordergrund zurückkehrt. Die Sitzungsdauer wird von der Öffnung der App oder dem Vordergrund bis zum Schließen der App oder dem Hintergrund gemessen.

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

Um einen asynchronen Stream zu abonnieren, können Sie [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) stattdessen verwenden.

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

{% tab Internet %}
Zur Zeit wird das Abonnieren von Sitzungs-Updates für das Internet Braze SDK nicht unterstützt.
{% endtab %}
{% endtabs %}

### Schritt 2: Tracking von Testsitzungen (optional)

Um das Tracking von Sitzungen zu testen, starten Sie eine Sitzung auf Ihrem Gerät, öffnen Sie dann das Braze-Dashboard und suchen Sie nach dem entsprechenden Nutzer:in. Wählen Sie in ihrem Nutzerprofil die **Übersicht über die Sitzungen** aus. Wenn die Metriken wie erwartet aktualisiert werden, funktioniert das Session Tracking korrekt.

![Die Übersicht über die Sitzungen eines Nutzerprofils, die die Anzahl der Sitzungen, das Datum der letzten Nutzung und das Datum der ersten Nutzung anzeigt.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
App-spezifische Details werden nur für Nutzer:innen angezeigt, die mehr als eine App verwendet haben.
{% endalert %}

## Ändern des Standard-Timeouts für Sitzungen {#change-session-timeout}

Sie können die Zeitspanne ändern, die vergeht, bevor eine Sitzung automatisch beendet wird.

{% tabs %}
{% tab android %}
Standardmäßig ist das Sitzungs-Timeout auf `10` Sekunden eingestellt. Um dies zu ändern, öffnen Sie Ihre Datei `braze.xml` und fügen Sie den Parameter `com_braze_session_timeout` hinzu. Sie kann auf eine beliebige ganze Zahl größer oder gleich `1` gesetzt werden.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab schnell %}
Standardmäßig ist das Sitzungs-Timeout auf `10` Sekunden eingestellt. Um dies zu ändern, setzen Sie `sessionTimeout` in dem `configuration` Objekt, das an [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class). Sie kann auf eine beliebige ganze Zahl größer oder gleich `1` gesetzt werden.

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

{% tab Internet %}
Standardmäßig ist das Sitzungs-Timeout auf `30` Sekunden eingestellt. Um dies zu ändern, übergeben Sie die Option `sessionTimeoutInSeconds` an Ihre [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) Funktion. Sie kann auf eine beliebige ganze Zahl größer oder gleich `1` gesetzt werden. 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Sie eine Sitzungszeitüberschreitung festlegen, werden alle Sitzungssemantiken automatisch bis zur festgelegten Zeitüberschreitung verlängert.
{% endalert %}
