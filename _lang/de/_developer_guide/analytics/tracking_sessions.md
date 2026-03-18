---
nav_title: Sitzungen verfolgen
article_title: Verfolgen Sie Sitzungen über das Braze SDK.
page_order: 3.3
description: "Erfahren Sie, wie Sie Sitzungen über das Braze SDK tracken können."

---

# Sitzungen verfolgen

> Erfahren Sie, wie Sie Sitzungen über das Braze SDK tracken können.

{% alert note %}
Für Wrapper-SDKs, die nicht aufgeführt sind, verwenden Sie stattdessen die entsprechende native Android- oder Swift-Methode.
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Definition von Inaktivität

Das Verständnis, wie Inaktivität definiert und gemessen wird, ist entscheidend für die effektive Verwaltung von Sitzungslebenszyklen im Internet SDK. Inaktivität bezeichnet einen Zeitraum, in dem das Braze Web SDK keine verfolgten Ereignisse der Nutzer:innen erkennt.

### Wie Inaktivität gemessen wird

Das Internet-SDK führt Tracking durch auf der Grundlage von [SDK-verfolgten Ereignissen]({{site.baseurl}}/user_guide/data/activation/custom_data/events/#events). Das SDK verfügt über einen internen Timer, der bei jedem Senden eines Ereignisses des Tracking-Prozesses zurückgesetzt wird. Wenn innerhalb der konfigurierten Zeitüberschreitung keine vom SDK verfolgten Ereignisse auftreten, wird die Sitzung als inaktiv betrachtet und beendet.

Weitere Informationen zur Implementierung des Sitzungslebenszyklus im Web-SDK finden Sie im Code für die Sitzungsverwaltung im [GitHub-Repository](https://github.com/braze-inc/braze-web-sdk/blob/master/src/session.ts) des [Braze Web-SDK](https://github.com/braze-inc/braze-web-sdk/blob/master/src/session.ts).

**Was gilt als Standard-Aktivität:**
- Öffnung oder Aktualisierung der Web-App
- Interaktion mit Braze-gesteuerten UI-Elementen (wie [In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/) oder [Content-Cards]({{site.baseurl}}/developer_guide/content_cards/))
- Aufruf von SDK-Methoden, die verfolgte Ereignisse senden (z. B. [angepasste Events]({{site.baseurl}}/developer_guide/analytics/logging_events/) oder [Updates von Benutzerattributen]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/))

**Was gilt als Standard nicht als Aktivität:**
- Wechseln zu einem anderen Browser-Tab
- Das Browserfenster minimieren
- Browser-Fokus- oder Unschärfeereignisse
- Scrollen oder Mausbewegungen auf der Seite

{% alert note %}
Das Web-SDK verfolgt nicht automatisch Änderungen der Browser-Sichtbarkeit, das Wechseln zwischen Tabs oder den Fokus der Nutzer:innen. Sie können diese Interaktionen auf Browser-Ebene jedoch verfolgen, indem Sie angepasste Event-Listener mithilfe der [Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) des Browsers implementieren und [angepasste Events]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web) an Braze senden. Ein Beispiel für die Implementierung finden Sie unter [Tracking benutzerdefinierter Inaktivität](#tracking-custom-inactivity).
{% endalert %}

### Konfiguration der Sitzungszeitüberschreitung

Standardmäßig betrachtet das Internet-SDK eine Sitzung nach 30 Minuten ohne verfolgte Ereignisse als inaktiv. Sie können diesen Schwellenwert bei der Initialisierung des SDK mithilfe des`sessionTimeoutInSeconds`Parameters anpassen. Ausführliche Informationen zur Konfiguration dieses Parameters, einschließlich Code-Beispielen, finden Sie unter [Ändern der Standard-Sitzungszeitüberschreitung](#changing-the-default-session-timeout).

### Beispiel: Szenarien der Inaktivität verstehen

Betrachten Sie das folgende Szenario:

1. Ein Nutzer:in öffnet Ihre Website, und das SDK startet eine Sitzung, indem es aufruft[`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession).
2. Die Nutzer:innen wechseln für 30 Minuten zu einem anderen Browser-Tab, um eine andere Website aufzurufen.
3. Während dieser Zeit werden auf Ihrer Website keine SDK-verfolgten Ereignisse erfasst.
4. Nach 30 Minuten Inaktivität wird die Sitzung automatisch beendet.
5. Wenn der Nutzer:in zurück zum Tab Ihrer Website wechselt und ein SDK-Ereignis triggert (z. B. das Anzeigen einer Seite oder die Interaktion mit Inhalten), beginnt eine neue Sitzung.

### Tracking benutzerdefinierter Inaktivität

Sollten Sie Tracking basierend auf der Sichtbarkeit des Browsers oder dem Wechseln von Tabs verfolgen müssen, implementieren Sie bitte angepasste Event-Listener in Ihrem JavaScript-Code. Verwenden Sie Browser-Ereignisse wie [URL],`visibilitychange`um zu erkennen, wann Nutzer:innen Ihre Seite verlassen, und senden Sie manuell [angepasste Events]({{site.baseurl}}/developer_guide/analytics/logging_events/) an Braze oder rufen Sie [[`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession)URL] auf, wenn dies angemessen ist.

```javascript
// Example: Track when user switches away from tab
document.addEventListener('visibilitychange', function() {
  if (document.hidden) {
    // User switched away - optionally log a custom event
    braze.logCustomEvent('tab_hidden');
  } else {
    // User returned - optionally start a new session and/or log an event
    // braze.openSession();
    braze.logCustomEvent('tab_visible');
  }
});
```

Weitere Informationen zum Protokollieren angepasster Events finden Sie unter [Protokollieren angepasster Events]({{site.baseurl}}/developer_guide/analytics/logging_events/). Weitere Informationen zum Sitzungslebenszyklus und zur Konfiguration der Zeitüberschreitung werden in der Referenz zu [Ändern der Standard-Sitzungszeitüberschreitung](#change-session-timeout) referenziert.

## Updates für Sitzungen abonnieren

### Schritt 1: Updates abonnieren

Um Updates für Sitzungen zu abonnieren, verwenden Sie die Methode `subscribeToSessionUpdates()`.

{% tabs %}
{% tab web %}
Zur Zeit wird das Abonnieren von Sitzungs-Updates für das Internet Braze SDK nicht unterstützt.
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

{% tab react native %}
Das React Native SDK stellt keine Methode zur Verfügung, um Session-Updates direkt zu abonnieren. Der Lebenszyklus der Sitzung wird vom zugrunde liegenden nativen SDK verwaltet. Um Updates abonnieren zu können, verwenden Sie bitte den nativen Plattformansatz für das **Android-** oder **SWIFT**-Tab.
{% endtab %}
{% endtabs %}

### Schritt 2: Tracking von Testsitzungen (optional)

Um das Tracking von Sitzungen zu testen, starten Sie eine Sitzung auf Ihrem Gerät, öffnen Sie dann das Braze-Dashboard und suchen Sie nach dem entsprechenden Nutzer:in. Wählen Sie in ihrem Nutzerprofil die **Übersicht über die Sitzungen** aus. Wenn die Metriken wie erwartet aktualisiert werden, funktioniert das Session Tracking korrekt.

![Der Abschnitt „Übersicht der Sitzungen“ eines Nutzerprofils zeigt die Anzahl der Sitzungen, das Datum der letzten Nutzung und das Datum der ersten Nutzung an.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
App-spezifische Details werden nur für Nutzer:innen angezeigt, die mehr als eine App verwendet haben.
{% endalert %}

## Ändern des Standard-Timeouts für Sitzungen {#change-session-timeout}

Sie können die Zeitspanne ändern, die vergeht, bevor eine Sitzung automatisch beendet wird.

{% tabs %}
{% tab web %}
Standardmäßig ist das Sitzungs-Timeout auf `30` Minuten eingestellt. Um dies zu ändern, übergeben Sie die Option `sessionTimeoutInSeconds` an Ihre [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) Funktion. Sie kann auf eine beliebige ganze Zahl größer oder gleich `1` gesetzt werden. 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

{% tab android %}
Standardmäßig ist das Sitzungs-Timeout auf `10` Sekunden eingestellt. Um dies zu ändern, öffnen Sie Ihre Datei `braze.xml` und fügen Sie den Parameter `com_braze_session_timeout` hinzu. Sie kann auf eine beliebige ganze Zahl größer oder gleich `1` gesetzt werden.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
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

{% tab react native %}
Das React Native SDK stützt sich auf die nativen SDKs, um Sitzungen zu verwalten. Um die Standard-Sitzungszeitüberschreitung zu ändern, konfigurieren Sie diese bitte in der nativen Ebene:

- **Android:** Bitte legen Sie dies`com_braze_session_timeout`in Ihrer`braze.xml`Datei fest. Für weitere Informationen wählen Sie bitte den Tab **„Android**“.
- **iOS:** Bitte stellen Sie Ihr`Braze.Configuration``sessionTimeout`Objekt auf. Für weitere Informationen wählen Sie bitte den Tab **„SWIFT**“.
{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Sie eine Sitzungszeitüberschreitung festlegen, werden alle Sitzungssemantiken automatisch bis zur festgelegten Zeitüberschreitung verlängert.
{% endalert %}
