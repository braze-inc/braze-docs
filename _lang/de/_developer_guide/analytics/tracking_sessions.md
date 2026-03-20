---
nav_title: Sitzungen verfolgen
article_title: Sitzungen über das Braze SDK verfolgen
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

Das Verständnis, wie Inaktivität definiert und gemessen wird, ist entscheidend für die effektive Verwaltung von Sitzungslebenszyklen im Internet SDK. Inaktivität bezeichnet einen Zeitraum, in dem das Braze Internet SDK keine getrackten Events von Nutzer:innen erkennt.

### Wie Inaktivität gemessen wird

Das Internet SDK trackt Inaktivität auf der Grundlage von [SDK-getrackten Events]({{site.baseurl}}/user_guide/data/activation/custom_data/events/#events). Das SDK verfügt über einen internen Timer, der bei jedem Senden eines getrackten Events zurückgesetzt wird. Wenn innerhalb des konfigurierten Timeout-Zeitraums keine vom SDK getrackten Events auftreten, wird die Sitzung als inaktiv betrachtet und beendet.

Weitere Informationen zur Implementierung des Sitzungslebenszyklus im Internet SDK finden Sie im Quellcode für die Sitzungsverwaltung im [GitHub-Repository des Braze Internet SDK](https://github.com/braze-inc/braze-web-sdk/blob/master/src/session.ts).

**Was standardmäßig als Aktivität zählt:**
- Öffnen oder Aktualisieren der Web-App
- Interaktion mit Braze-gesteuerten UI-Elementen (wie [In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/) oder [Content-Cards]({{site.baseurl}}/developer_guide/content_cards/))
- Aufruf von SDK-Methoden, die getrackte Events senden (z. B. [angepasste Events]({{site.baseurl}}/developer_guide/analytics/logging_events/) oder [Updates von Nutzerattributen]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/))

**Was standardmäßig nicht als Aktivität zählt:**
- Wechseln zu einem anderen Browser-Tab
- Minimieren des Browserfensters
- Browser-Fokus- oder Blur-Events
- Scrollen oder Mausbewegungen auf der Seite

{% alert note %}
Das Internet SDK trackt nicht automatisch Änderungen der Browser-Sichtbarkeit, Tab-Wechsel oder den Nutzerfokus. Sie können diese Interaktionen auf Browser-Ebene jedoch tracken, indem Sie angepasste Event-Listener mithilfe der [Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) des Browsers implementieren und [angepasste Events]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web) an Braze senden. Ein Beispiel für die Implementierung finden Sie unter [Tracking angepasster Inaktivität](#tracking-custom-inactivity).
{% endalert %}

### Konfiguration des Sitzungs-Timeouts

Standardmäßig betrachtet das Internet SDK eine Sitzung nach 30 Minuten ohne getrackte Events als inaktiv. Sie können diesen Schwellenwert bei der Initialisierung des SDK mithilfe des Parameters `sessionTimeoutInSeconds` anpassen. Ausführliche Informationen zur Konfiguration dieses Parameters, einschließlich Code-Beispielen, finden Sie unter [Ändern des Standard-Sitzungs-Timeouts](#changing-the-default-session-timeout).

### Beispiel: Szenarien der Inaktivität verstehen

Betrachten Sie das folgende Szenario:

1. Eine Nutzer:in öffnet Ihre Website, und das SDK startet eine Sitzung, indem es [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession) aufruft.
2. Die Nutzer:in wechselt für 30 Minuten zu einem anderen Browser-Tab, um eine andere Website aufzurufen.
3. Während dieser Zeit werden auf Ihrer Website keine SDK-getrackten Events erfasst.
4. Nach 30 Minuten Inaktivität wird die Sitzung automatisch beendet.
5. Wenn die Nutzer:in zurück zum Tab Ihrer Website wechselt und ein SDK-Event triggert (z. B. das Anzeigen einer Seite oder die Interaktion mit Inhalten), beginnt eine neue Sitzung.

### Tracking angepasster Inaktivität

Sollten Sie Inaktivität basierend auf der Sichtbarkeit des Browsers oder dem Tab-Wechsel tracken müssen, implementieren Sie angepasste Event-Listener in Ihrem JavaScript-Code. Verwenden Sie Browser-Events wie `visibilitychange`, um zu erkennen, wann Nutzer:innen Ihre Seite verlassen, und senden Sie manuell [angepasste Events]({{site.baseurl}}/developer_guide/analytics/logging_events/) an Braze oder rufen Sie [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession) auf, wenn dies angemessen ist.

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

Weitere Informationen zum Protokollieren angepasster Events finden Sie unter [Angepasste Events protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_events/). Weitere Informationen zum Sitzungslebenszyklus und zur Timeout-Konfiguration finden Sie unter [Ändern des Standard-Sitzungs-Timeouts](#change-session-timeout).

## Sitzungs-Updates abonnieren

### 1. Schritt: Updates abonnieren

Um Sitzungs-Updates zu abonnieren, verwenden Sie die Methode `subscribeToSessionUpdates()`.

{% tabs %}
{% tab web %}
Derzeit wird das Abonnieren von Sitzungs-Updates für das Braze Internet SDK nicht unterstützt.
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
Wenn Sie einen Callback für das Sitzungsende registrieren, wird dieser ausgelöst, wenn die App in den Vordergrund zurückkehrt. Die Sitzungsdauer wird ab dem Öffnen oder In-den-Vordergrund-Bringen der App bis zum Schließen oder In-den-Hintergrund-Wechseln gemessen.

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

Um einen asynchronen Stream zu abonnieren, können Sie stattdessen [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) verwenden.

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
Das React Native SDK stellt keine Methode zur Verfügung, um Sitzungs-Updates direkt zu abonnieren. Der Sitzungslebenszyklus wird vom zugrunde liegenden nativen SDK verwaltet. Um Updates zu abonnieren, verwenden Sie den nativen Plattformansatz für den Tab **Android** oder **Swift**.
{% endtab %}
{% endtabs %}

### 2. Schritt: Sitzungs-Tracking testen (optional)

Um das Sitzungs-Tracking zu testen, starten Sie eine Sitzung auf Ihrem Gerät, öffnen Sie dann das Braze-Dashboard und suchen Sie nach der entsprechenden Nutzer:in. Wählen Sie in ihrem Nutzerprofil die **Sitzungsübersicht** aus. Wenn die Metriken wie erwartet aktualisiert werden, funktioniert das Sitzungs-Tracking korrekt.

![Der Abschnitt „Sitzungsübersicht" eines Nutzerprofils zeigt die Anzahl der Sitzungen, das Datum der letzten Nutzung und das Datum der ersten Nutzung an.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
App-spezifische Details werden nur für Nutzer:innen angezeigt, die mehr als eine App verwendet haben.
{% endalert %}

## Ändern des Standard-Sitzungs-Timeouts {#change-session-timeout}

Sie können die Zeitspanne ändern, die vergeht, bevor eine Sitzung automatisch beendet wird.

{% tabs %}
{% tab web %}
Standardmäßig ist das Sitzungs-Timeout auf `30` Minuten eingestellt. Um dies zu ändern, übergeben Sie die Option `sessionTimeoutInSeconds` an Ihre [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)-Funktion. Der Wert kann auf eine beliebige ganze Zahl größer oder gleich `1` gesetzt werden. 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

{% tab android %}
Standardmäßig ist das Sitzungs-Timeout auf `10` Sekunden eingestellt. Um dies zu ändern, öffnen Sie Ihre Datei `braze.xml` und fügen Sie den Parameter `com_braze_session_timeout` hinzu. Der Wert kann auf eine beliebige ganze Zahl größer oder gleich `1` gesetzt werden.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
Standardmäßig ist das Sitzungs-Timeout auf `10` Sekunden eingestellt. Um dies zu ändern, setzen Sie `sessionTimeout` in dem `configuration`-Objekt, das an [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class) übergeben wird. Der Wert kann auf eine beliebige ganze Zahl größer oder gleich `1` gesetzt werden.

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
Das React Native SDK stützt sich auf die nativen SDKs, um Sitzungen zu verwalten. Um das Standard-Sitzungs-Timeout zu ändern, konfigurieren Sie es in der nativen Ebene:

- **Android:** Setzen Sie `com_braze_session_timeout` in Ihrer `braze.xml`-Datei. Für weitere Informationen wählen Sie den Tab **Android**.
- **iOS:** Setzen Sie `sessionTimeout` in Ihrem `Braze.Configuration`-Objekt. Für weitere Informationen wählen Sie den Tab **Swift**.
{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Sie ein Sitzungs-Timeout festlegen, werden alle Sitzungssemantiken automatisch auf das festgelegte Timeout erweitert.
{% endalert %}

## Fehlerbehebung

### Nutzerprofil zeigt 0 Sitzungen

Ein Nutzerprofil kann 0 Sitzungen aufweisen, wenn die Nutzer:in außerhalb des SDK erstellt wurde:

- **Über REST API erstellt:** Wenn eine Nutzer:in über den Endpunkt [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) mit einer `app_id` in der Anfrage erstellt wird, erscheint das Profil zwar mit dieser App verknüpft, hat aber keine Sitzungsdaten, da das SDK für diese Nutzer:in nie initialisiert wurde.
- **Über CSV-Import erstellt:** Wenn eine Nutzer:in per [CSV]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) ohne Werte für die Felder der ersten oder letzten Sitzung importiert wird, existiert das Profil mit 0 Sitzungen.