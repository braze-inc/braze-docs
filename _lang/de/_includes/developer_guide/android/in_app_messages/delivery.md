{% multi_lang_include developer_guide/prerequisites/android.md %}

## Nachrichten triggern

### Auslöser-Typen

In-App-Nachrichten werden automatisch getriggert, wenn das SDK einen der folgenden angepassten Event-Typen protokolliert: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` und `Push Click`. Beachten Sie, dass die Trigger `Specific Purchase` und `Custom Event` auch robuste Filter für Eigenschaften enthalten.

{% alert note %}
In-App-Nachrichten können nicht über die API oder durch API-Ereignisse ausgelöst werden, sondern nur durch angepasste Events, die vom SDK protokolliert werden. Wenn Sie mehr über die Protokollierung erfahren möchten, lesen Sie den Abschnitt [Protokollierung angepasster Events]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Semantik der Zustellung

Alle in Frage kommenden In-App-Nachrichten werden dem Gerät eines Nutzers:innen zu Beginn seiner Sitzung zugestellt. Wenn es zugestellt wird, holt das SDK die Assets im Voraus, so dass sie zum Zeitpunkt des Triggerns verfügbar sind und die Anzeige-Latenzzeit minimiert wird. Wenn das triggernde Ereignis mehr als eine in Frage kommende In-App-Nachricht hat, wird nur die Nachricht mit der höchsten Priorität zugestellt.

Weitere Informationen über die Semantik des SDK für den Sitzungsstart finden Sie unter [Sitzungslebenszyklus]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android).

### Rate-Limit

Standardmäßig begrenzen wir die Rate für In-App-Nachrichten auf einmal alle 30 Sekunden, um ein hochwertiges Nutzererlebnis zu unterstützen.

Um diesen Wert zu überschreiben, legen Sie `com_braze_trigger_action_minimum_time_interval_seconds` in `braze.xml` fest mittels:

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Schlüssel-Wert-Paare

Wenn Sie eine Kampagne in Braze erstellen, können Sie Schlüssel-Wert-Paare als `extras` festlegen, die das In-App-Nachricht-Objekt verwenden kann, um Daten an Ihre App zu senden. Zum Beispiel:

{% tabs %}
{% tab JAVA %}
```java
Map<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endtab %}
{% endtabs %}

{% alert note %}
Weitere Informationen finden Sie in der [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}

## Deaktivieren von automatischen Triggern

So verhindern Sie, dass In-App-Nachrichten automatisch ausgelöst werden:

1. Stellen Sie sicher, dass Sie die automatische Initialisierung der Integration verwenden, die ab Version `2.2.0` standardmäßig aktiviert ist.
2. Setzen Sie die Standardeinstellung für In-App-Nachrichten auf `DISCARD`, indem Sie die folgende Zeile in Ihre Datei `braze.xml` einfügen.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

## Manuelles Auslösen von Nachrichten

Standardmäßig werden In-App-Nachrichten automatisch getriggert, wenn das SDK ein angepasstes Event protokolliert. Sie können jedoch eine Nachricht mit den folgenden Methoden manuell triggern.

### Ein serverseitiges Ereignis verwenden

Um eine In-App-Nachricht über ein vom Server gesendetes Ereignis auszulösen, senden Sie eine stille Push-Benachrichtigung an das Gerät, die einen angepassten Push-Callback zur Protokollierung eines SDK-basierten Ereignisses ermöglicht. Dieses Ereignis triggert dann die In-App-Nachricht für den Nutzer:innen.

#### Schritt 1: Erstellen Sie einen Push-Callback, um den stillen Push zu empfangen

Registrieren Sie [Ihren angepassten Push-Callback]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#push-callback), um auf eine bestimmte stille Push-Benachrichtigung zu warten.

Im folgenden Beispiel werden zwei Ereignisse für die zuzustellende In-App-Nachricht protokolliert, eines vom Server und eines von Ihrem angepassten Push-Callback. Um sicherzustellen, dass dasselbe Event nicht doppelt vorkommt, sollte das von Ihrem Push Callback protokollierte Event einer generischen Namenskonvention folgen, z. B. "In-App-Nachricht triggern", und nicht denselben Namen tragen wie das vom Server gesendete Event. Andernfalls können die Segmentierung und die Nutzerdaten dadurch beeinträchtigt werden, dass für eine einzelne Nutzer:innen-Aktion doppelte Ereignisse protokolliert werden.

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

#### Schritt 2: Erstellen Sie eine Push-Kampagne

Erstellen Sie eine [stille Push-Kampagne]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android), die über das vom Server gesendete Event getriggert wird.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

Die Push-Kampagne muss Schlüssel-Wert-Paare enthalten, die angeben, dass diese Push-Kampagne gesendet wird, um ein angepasstes SDK-Event zu protokollieren. Dieses Event wird verwendet, um die In-App-Nachricht zu triggern.

![Zwei Sätze von Schlüssel-Wert-Paaren: IS_SERVER_EVENT auf "true" und CAMPAIGN_NAME auf "example campaign name" gesetzt.]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

Der frühere Code für den Push Callback erkennt die Schlüssel-Wert-Paare und protokolliert das entsprechende angepasste SDK-Event.

Wenn Sie Ihrem "In-App-Nachricht triggern"-Event Event-Eigenschaften hinzufügen möchten, können Sie diese in den Schlüssel-Wert-Paaren des Push-Payloads übergeben. In diesem Beispiel wurde der Kampagnen-Name der nachfolgenden In-App-Nachricht eingefügt. Ihr angepasster Push Callback kann dann bei der Protokollierung des angepassten Events den Wert als Parameter der Event-Eigenschaft übergeben.

#### Schritt 3: In-App-Kampagne erstellen

Erstellen Sie Ihre für Nutzer sichtbare In-App-Nachricht-Kampagne im Braze-Dashboard. Diese Kampagne sollte eine aktionsbasierte Zustellung haben und durch das angepasste Event ausgelöst werden, das in Ihrem Push-Callback protokolliert wird.

Im folgenden Beispiel wurde die zu triggernde In-App-Nachricht konfiguriert, indem die Event-Eigenschaft im Rahmen des usprünglichen stillen Push gesendet wurde.

![Eine aktionsbasierte Zustellung, bei der eine In-App-Nachricht ausgelöst wird, wenn "campaign_name" gleich "IAM-Kampagnenname Beispiel" ist.]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Wenn ein vom Server gesendetes Event protokolliert wird, während sich die App nicht im Vordergrund befindet, wird das Event protokolliert, aber die In-App-Nachricht wird nicht angezeigt. Wenn Sie möchten, dass das Event verzögert wird, bis die Anwendung im Vordergrund ist, müssen Sie in Ihrem angepassten Push-Empfänger ein Häkchen setzen, um das Event zu verwerfen oder zu verzögern, bis die App in den Vordergrund getreten ist.

### Anzeige einer vordefinierten Nachricht

Um eine vordefinierte In-App-Nachricht manuell anzuzeigen, verwenden Sie die folgende Methode:

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

### Anzeige einer Nachricht in Realtime 

Sie können auch In-App-Nachrichten in Echtzeit erstellen und anzeigen, indem Sie dieselben Lokalisierungsoptionen nutzen, die auch auf dem Dashboard zur Verfügung stehen. Um dies zu tun:

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
