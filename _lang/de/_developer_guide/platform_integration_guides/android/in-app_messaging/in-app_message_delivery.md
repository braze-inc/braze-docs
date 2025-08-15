---
nav_title: Zustellung von In-App-Nachrichten
article_title: In-App-Zustellung von Nachrichten für Android und FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Dieser Referenzartikel beschreibt die Zustellung von Android- und FireOS-In-App-Nachrichten. Außerdem behandelt er verschiedene Trigger-Typen, Zustellungssemantiken und Schritte zur Auslösung von Events."
channel:
  - in-app messages

---

# Zustellung von In-App-Nachrichten

> Dieser Referenzartikel beschreibt die Zustellung von Android- und FireOS-In-App-Nachrichten. Außerdem behandelt er verschiedene Trigger-Typen, Zustellungssemantiken und Schritte zur Auslösung von Events.

## Auslöser-Typen

Mit unserem Produkt für In-App-Nachrichten können Sie die Anzeige von In-App-Nachrichten infolge verschiedener Event-Typen auslösen: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` und `Push Click`. Außerdem können `Specific Purchase`- und `Custom Event`\- Trigger robuste Eigenschaftsfilter enthalten.

{% alert note %}
Ausgelöste In-App-Nachrichten funktionieren nur bei angepassten Events, die über das Braze SDK protokolliert werden. In-App-Nachrichten können nicht über die API oder durch API-Event (wie Kauf-Events) getriggert werden. Sehen Sie sich an, wie Sie [angepasste Events protokollieren]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/) können.
{% endalert %}

## Semantik der Zustellung

Alle In-App-Nachrichten, für die ein Nutzer:innen berechtigt ist, werden dem Gerät des Nutzers zugestellt, sobald [die Sitzung beginnt]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle). Bei der Zustellung ruft das SDK die Assets mittels Prefetching ab, damit sie zum Trigger-Zeitpunkt sofort verfügbar sind und die Anzeige-Latenzzeit minimiert wird.

Wenn ein Trigger-Event mit mehr als einer in Frage kommenden In-App-Nachricht verbunden ist, wird nur die In-App-Nachricht mit der höchsten Priorität zugestellt.

Bei In-App-Nachrichten, die sofort nach der Zustellung angezeigt werden (Sitzungsstart, Push-Klick), kann es zu einer gewissen Latenz kommen, da die Assets nicht mittels Prefetching abgerufen werden.

## Mindestzeitintervall zwischen Auslösern

Standardmäßig begrenzen wir die Rate für In-App-Nachrichten auf einmal alle 30 Sekunden, um ein hochwertiges Nutzererlebnis zu unterstützen.

Um diesen Wert zu überschreiben, legen Sie `com_braze_trigger_action_minimum_time_interval_seconds` in `braze.xml` fest mittels:

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Serverseitiges Event-Triggering

Standardmäßig werden In-App-Nachrichten durch angepasste Events getriggert, die vom SDK protokolliert werden. Sie können In-App-Nachrichten jedoch auch durch vom Server gesendete Events auslösen.

Um dieses Feature zu aktivieren, wird ein stiller Push an das Gerät gesendet, der einen angepassten Push-Callback zur Protokollierung eines SDK-basierten Events erlaubt. Dieses SDK-Event triggert anschließend die In-App-Nachricht, die dem Nutzer zugeht.

### Schritt 1: Erstellen Sie einen Push-Callback, um den stillen Push zu empfangen

Registrieren Sie Ihren angepassten Push-Callback, um auf eine bestimmte stille Push-Benachrichtigung zu warten. Weitere Informationen finden Sie unter [Standard Android Push Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback).

Für die zuzustellende In-App-Nachricht werden zwei Events protokolliert, eines vom Server und eines von Ihrem angepassten Push-Callback. Um sicherzustellen, dass dasselbe Event nicht doppelt vorkommt, sollte das von Ihrem Push Callback protokollierte Event einer generischen Namenskonvention folgen, z. B. "In-App-Nachricht triggern", und nicht denselben Namen tragen wie das vom Server gesendete Event. Andernfalls können die Segmentierung und die Nutzerdaten dadurch beeinträchtigt werden, dass für eine einzelne Nutzer:innen-Aktion doppelte Ereignisse protokolliert werden.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endtab %}
{% endtabs %}

### Schritt 2: Erstellen Sie eine Push-Kampagne

Erstellen Sie eine [stille Push-Kampagne]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/), die über das vom Server gesendete Event getriggert wird.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

Die Push-Kampagne muss Schlüssel-Wert-Paare enthalten, die angeben, dass diese Push-Kampagne gesendet wird, um ein angepasstes SDK-Event zu protokollieren. Dieses Event wird verwendet, um die In-App-Nachricht zu triggern.

![Zwei Sätze von Schlüssel-Wert-Paaren: IS_SERVER_EVENT auf "true" und CAMPAIGN_NAME auf "example campaign name" gesetzt.]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

Der frühere Code für den Push Callback erkennt die Schlüssel-Wert-Paare und protokolliert das entsprechende angepasste SDK-Event.

Wenn Sie Ihrem "In-App-Nachricht triggern"-Event Event-Eigenschaften hinzufügen möchten, können Sie diese in den Schlüssel-Wert-Paaren des Push-Payloads übergeben. In diesem Beispiel wurde der Kampagnen-Name der nachfolgenden In-App-Nachricht eingefügt. Ihr angepasster Push Callback kann dann bei der Protokollierung des angepassten Events den Wert als Parameter der Event-Eigenschaft übergeben.

### Schritt 3: In-App-Kampagne erstellen

Erstellen Sie Ihre für Nutzer sichtbare In-App-Nachricht-Kampagne im Braze-Dashboard. Diese Kampagne sollte eine aktionsbasierte Zustellung haben und durch das angepasste Event ausgelöst werden, das in Ihrem Push-Callback protokolliert wird.

Im folgenden Beispiel wurde die zu triggernde In-App-Nachricht konfiguriert, indem die Event-Eigenschaft im Rahmen des usprünglichen stillen Push gesendet wurde.

![Eine aktionsbasierte Zustellung, bei der eine In-App-Nachricht ausgelöst wird, wenn "campaign_name" gleich "IAM-Kampagnenname Beispiel" ist.]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Wenn ein vom Server gesendetes Event protokolliert wird, während sich die App nicht im Vordergrund befindet, wird das Event protokolliert, aber die In-App-Nachricht wird nicht angezeigt. Wenn Sie möchten, dass das Event verzögert wird, bis die Anwendung im Vordergrund ist, müssen Sie in Ihrem angepassten Push-Empfänger ein Häkchen setzen, um das Event zu verwerfen oder zu verzögern, bis die App in den Vordergrund getreten ist.

## Lokale In-App-Nachrichten

In-App-Nachrichten können innerhalb der App erstellt und lokal in Realtime angezeigt werden. Alle auf dem Dashboard verfügbaren Lokalisierungsoptionen sind auch lokal verfügbar. Dies ist besonders nützlich für die Anzeige von Nachrichten, die Sie in Echtzeit in der App auslösen möchten.

{% tabs %}
{% tab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endtab %}
{% endtabs %}

{% alert important %}
Zeigen Sie keine In-App-Nachrichten an, wenn die Softtastatur auf dem Bildschirm angezeigt wird, da das Rendering unter diesen Umständen undefiniert ist.
{% endalert %}

### Manuelles Auslösen der Anzeige von In-App-Nachrichten

Mit der folgenden Methode können Sie Ihre In-App-Nachricht manuell anzeigen lassen:

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endtab %}
{% endtabs %}

