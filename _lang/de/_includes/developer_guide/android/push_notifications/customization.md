{% multi_lang_include developer_guide/prerequisites/android.md %} Sie müssen auch [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Verwendung eines Callbacks für Push-Ereignisse {#push-callback}

Braze stellt einen [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) Callback bereit, wenn Push-Benachrichtigungen empfangen, geöffnet oder verworfen werden. Es wird empfohlen, diesen Callback in Ihrem `Application.onCreate()` zu platzieren, um keine Events zu verpassen, die auftreten, während Ihre Anwendung nicht läuft.

{% alert note %}
Wenn Sie bisher einen angepassten Broadcast-Empfänger für diese Funktion in Ihrer Anwendung verwendet haben, können Sie ihn zugunsten dieser Integrationsoption entfernen.
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final BrazeNotificationPayload parsedData = event.getNotificationPayload();

  //
  // The type of notification itself
  //
  final boolean isPushOpenEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_OPENED;
  final boolean isPushReceivedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_RECEIVED;
  // Sent when a user has dismissed a notification
  final boolean isPushDeletedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_DELETED;

  //
  // Notification data
  //
  final String pushTitle = parsedData.getTitleText();
  final Long pushArrivalTimeMs = parsedData.getNotificationReceivedTimestampMillis();
  final String deeplink = parsedData.getDeeplink();

  //
  // Custom KVP data
  //
  final String myCustomKvp1 = parsedData.getBrazeExtras().getString("my first kvp");
  final String myCustomKvp2 = parsedData.getBrazeExtras().getString("my second kvp");
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).subscribeToPushNotificationEvents { event ->
    val parsedData = event.notificationPayload

    //
    // The type of notification itself
    //
    val isPushOpenEvent = event.eventType == BrazePushEventType.NOTIFICATION_OPENED
    val isPushReceivedEvent = event.eventType == BrazePushEventType.NOTIFICATION_RECEIVED
    // Sent when a user has dismissed a notification
    val isPushDeletedEvent = event.eventType == BrazePushEventType.NOTIFICATION_DELETED

    //
    // Notification data
    //
    val pushTitle = parsedData.titleText
    val pushArrivalTimeMs = parsedData.notificationReceivedTimestampMillis
    val deeplink = parsedData.deeplink

    //
    // Custom KVP data
    //
    val myCustomKvp1 = parsedData.brazeExtras.getString("my first kvp")
    val myCustomKvp2 = parsedData.brazeExtras.getString("my second kvp")
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Bei Aktions-Buttons für Benachrichtigungen werden die `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` Absichten ausgelöst, wenn Buttons mit den Aktionen `opens app` oder `deep link` angeklickt werden. Die Handhabung von Deeplinks und Extras bleibt unverändert. Buttons mit `close`-Aktionen lösen keine `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED`-Absichten aus und beenden die Benachrichtigung automatisch.
{% endalert %}

{% alert important %}
Erstellen Sie Ihren Listener für Push-Benachrichtigungen in `Application.onCreate`, um sicherzustellen, dass er getriggert wird, wenn auf eine Benachrichtigung getippt wird, während sich Ihre App in einem beendeten Zustand befindet.
{% endalert %}

## Anzeige der Benachrichtigung anpassen {#customization-display}

### Schritt 1: Angepasste Benachrichtigungs-Factory erstellen

In manchen Szenarien möchten Sie Push-Benachrichtigungen auf eine Weise anpassen, die auf dem Server umständlich oder nicht verfügbar wäre. Um Ihnen die vollständige Kontrolle über die Display-Anzeige zu geben, haben wir die Möglichkeit hinzugefügt, Ihre eigenen [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html)-Benachrichtigungsobjekte für die Anzeige durch Braze zu erstellen.

Wenn eine angepasste `IBrazeNotificationFactory` eingestellt ist, ruft Braze beim Push-Empfang die Methode `createNotification()` Ihrer Factory auf, bevor die Benachrichtigung dem Nutzer angezeigt wird. Braze übergibt ein `Bundle` mit Push-Daten von Braze und ein weiteres `Bundle` mit angepassten Schlüssel-Wert-Paaren, die entweder über das Dashboard oder die Messaging APIs gesendet werden:

Braze übergibt eine [`BrazeNotificationPayload`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html) mit Daten aus der Push-Benachrichtigung von Braze.

{% tabs %}
{% tab JAVA %}

```java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Example of getting notification title
  String title = brazeNotificationPayload.getTitleText();

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Example of getting notification title
  val title = brazeNotificationPayload.getTitleText()

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key")
}
```

{% endtab %}
{% endtabs %}

Sie können `null` von Ihrer angepassten `createNotification()` Methode zurückgeben, um die Benachrichtigung überhaupt nicht anzuzeigen, `BrazeNotificationFactory.getInstance().createNotification()` verwenden, um unser Standard `notification` Objekt für diese Daten zu erhalten und es vor der Anzeige zu ändern, oder ein völlig separates `notification` Objekt für die Anzeige erzeugen.

{% alert note %}
Die Dokumentation zu den Push-Daten von Braze finden Sie im [Android SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html).
{% endalert %}

### Schritt 2: Angepasste Benachrichtigungs-Factory einstellen

Um Braze anzuweisen, Ihre angepasste Benachrichtigungs-Factory zu verwenden, stellen Sie mit der Methode `setCustomBrazeNotificationFactory` Ihre [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) ein:

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

Der empfohlene Ort, um Ihre angepasste `IBrazeNotificationFactory` einzustellen, ist in der Methode `Application.onCreate()` application lifecycle (nicht activity). Dies ermöglicht die korrekte Einstellung der Benachrichtigungsfabrik, wenn Ihr App-Prozess aktiv ist.

{% alert important %}
Das Erstellen einer eigenen Push-Benachrichtigung von Grund auf ist ein fortgeschrittener Anwendungsfall und sollte nur mit gründlichen Tests und einem tiefen Verständnis der Push-Funktionen von Braze durchgeführt werden. Sie müssen zum Beispiel sicherstellen, dass Ihre Push-Benachrichtigungen korrekt geöffnet werden.
{% endalert %}

Um Ihre angepasste [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) zu deaktivieren und zur Standard-Braze-Behandlung für Push zurückzukehren, übergeben Sie `null` an unseren angepassten Notification Factory Setter:

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## Rendering von mehrfarbigem Text

In Braze SDK Version 3.1.1 kann HTML an ein Gerät gesendet werden, um mehrfarbigen Text in Push-Benachrichtigungen darzustellen.

![Die Android-Push-Nachricht "Multicolor Push Test Nachricht", bei der die Buchstaben verschiedene Farben haben, kursiv geschrieben sind und eine Hintergrundfarbe haben.]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

Dieses Beispiel wird mit dem folgenden HTML-Code wiedergegeben:

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>

<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Denken Sie daran, dass Android einschränkt, welche HTML-Elemente und Tags in Ihren Push-Benachrichtigungen zulässig sind. Zum Beispiel ist `marquee` nicht zulässig.

{% alert important %}
Die Darstellung von mehrfarbigem Text ist gerätespezifisch und wird je nach Android-Gerät oder -Version möglicherweise nicht angezeigt.
{% endalert %}

Um mehrfarbigen Text in einer Push-Benachrichtigung darzustellen, können Sie Ihr `braze.xml` oder `BrazeConfig` aktualisieren:

{% tabs local %}
{% tab braze.xml %}
Fügen Sie Folgendes in Ihrem `braze.xml` hinzu:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```
{% endtab %}

{% tab BrazeConfig %}
Fügen Sie Folgendes in Ihrem [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% subtabs local %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Unterstützte HTML Tags

Derzeit listet Google die unterstützten HTML Tags für Android nicht direkt in der Dokumentation auf. Diese Informationen finden Sie nur in der [ `Html.java` Datei des Git-Repositorys.](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/Html.java) Beachten Sie dies, wenn Sie sich auf die folgende Tabelle beziehen, da diese Informationen aus dieser Datei stammen und sich die unterstützten HTML-Tags noch ändern können.

<table>
  <thead>
    <tr>
      <th>Kategorie</th>
      <th>HTML Tag</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">Grundlegende Textgestaltung</td>
      <td><code>&lt;b&gt;</code>, <code>&lt;strong&gt;</code></td>
      <td>Fettgedruckter Text</td>
    </tr>
    <tr>
      <td><code>&lt;i&gt;</code>, <code>&lt;em&gt;</code></td>
      <td>Kursiver Text</td>
    </tr>
    <tr>
      <td><code>&lt;u&gt;</code></td>
      <td>Text unterstreichen</td>
    </tr>
    <tr>
      <td><code>&lt;s&gt;</code>, <code>&lt;strike&gt;</code>, <code>&lt;del&gt;</code></td>
      <td>Durchgestrichener Text</td>
    </tr>
    <tr>
      <td><code>&lt;sup&gt;</code></td>
      <td>Hochgestellter Text</td>
    </tr>
    <tr>
      <td><code>&lt;sub&gt;</code></td>
      <td>Subskriptiver Text</td>
    </tr>
    <tr>
      <td><code>&lt;tt&gt;</code></td>
      <td>Einfarbiger Text</td>
    </tr>
    <tr>
      <td rowspan="3">Größe/Schrift</td>
      <td><code>&lt;big&gt;</code>, <code>&lt;small&gt;</code></td>
      <td>Relative Textgröße ändert sich</td>
    </tr>
    <tr>
      <td><code>&lt;font color="..."&gt;</code></td>
      <td>Legt die Vordergrundfarbe fest</td>
    </tr>
    <tr>
      <td><code>&lt;span&gt;</code> (mit Inline-CSS)</td>
      <td>Inline-Stile (e.g., Farbe, Hintergrund)</td>
    </tr>
    <tr>
      <td rowspan="4">Absatz &amp; Block</td>
      <td><code>&lt;p&gt;</code>, <code>&lt;div&gt;</code></td>
      <td>Abschnitte auf Blockebene</td>
    </tr>
    <tr>
      <td><code>&lt;br&gt;</code></td>
      <td>Zeilenumbruch</td>
    </tr>
    <tr>
      <td><code>&lt;blockquote&gt;</code></td>
      <td>Zitierter Block</td>
    </tr>
    <tr>
      <td><code>&lt;ul&gt;</code> + <code>&lt;li&gt;</code></td>
      <td>Ungeordnete Liste mit Aufzählungszeichen</td>
    </tr>
    <tr>
      <td>Rubriken</td>
      <td><code>&lt;h1&gt;</code> - <code>&lt;h6&gt;</code></td>
      <td>Überschriften (verschiedene Größen)</td>
    </tr>
    <tr>
      <td rowspan="2">Links &amp; Bilder</td>
      <td><code>&lt;a href="..."&gt;</code></td>
      <td>Anklickbarer Link</td>
    </tr>
    <tr>
      <td><code>&lt;img src="..."&gt;</code></td>
      <td>Inline-Bild</td>
    </tr>
    <tr>
      <td>Andere Inline</td>
      <td><code>&lt;em&gt;</code>, <code>&lt;strong&gt;</code>, <code>&lt;dfn&gt;</code>, <code>&lt;cite&gt;</code></td>
      <td>Synonyme für kursiv oder fett</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Rendering von Inline-Bildern

### Funktionsweise

Sie können ein größeres Bild in Ihrer Android Push-Benachrichtigung mit Hilfe von Inline Image Push präsentieren. Bei diesem Design müssen Nutzer die Push-Benachrichtigung nicht mehr manuell erweitern, um das Bild zu vergrößern. Im Gegensatz zu normalen Android-Push-Benachrichtigungen haben die Inline-Image-Push-Bilder ein Seitenverhältnis von 3:2.

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="max-width:50%;"}

### Kompatibilität

Sie können zwar Inline-Bilder an jedes Gerät senden, aber Geräte und SDKs, die die Mindestversionen nicht erfüllen, zeigen stattdessen ein Standardbild an. Damit Inline-Bilder korrekt angezeigt werden, benötigen Sie sowohl das Android Braze SDK v10.0.0+ als auch ein Gerät mit Android M+.

{% alert note %}
Geräte mit Android 12 werden aufgrund von Änderungen in den benutzerdefinierten Push-Benachrichtigungsstilen anders dargestellt.
{% endalert %}

### Push für ein Inline-Bild senden

Wenn Sie eine Android-Push-Nachricht erstellen, ist diese Funktion in der Dropdown-Liste **Benachrichtigungstyp** verfügbar.

![Der Push-Kampagnen-Editor zeigt die Position des Dropdown-Menüs "Benachrichtigungstyp" (oberhalb der Standard-Push-Vorschau).]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})

## Einstellungen

Für die Push-Benachrichtigungen von Android, die über das Braze-Dashboard versendet werden, sind viele fortschrittliche Einstellungen verfügbar. Dieser Artikel beschreibt diese Funktionen und wie Sie sie erfolgreich nutzen können.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### ID der Benachrichtigung {#notification-id}

Eine **Notification ID** ist ein eindeutiger Bezeichner für eine von Ihnen gewählte Nachrichtenkategorie, der dem Messaging-Dienst mitteilt, dass er nur die jüngste Nachricht mit dieser ID berücksichtigen soll. Wenn Sie eine ID für die Benachrichtigung festlegen, können Sie nur die aktuellste und relevante Nachricht versenden, anstatt einen Stapel veralteter, irrelevanter Nachrichten.

### Priorität der Firebase-Nachrichtenzustellung {#fcm-priority}

Mit dem Feld [Priorität der Firebase-Nachrichtenzustellung](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) können Sie festlegen, ob ein Push mit "normaler" oder "hoher" Priorität an Firebase Cloud Messaging gesendet wird.

### Lebenserwartung (TTL) {#ttl}

Im Feld **Time to Live** (TTL) können Sie eine benutzerdefinierte Zeitspanne für die Speicherung von Nachrichten mit dem Push-Messaging-Dienst festlegen. Die Standardwerte für die Time-To-Live betragen vier Wochen für FCM und 31 Tage für ADM.

### Zusammenfassender Text {#summary-text}

Mit dem Zusammenfassungstext können Sie zusätzlichen Text in der erweiterten Benachrichtigungsansicht einstellen. Es dient auch als Beschriftung für Benachrichtigungen mit Bildern.

![Eine Android Nachricht mit dem Titel "Dies ist der Titel der Benachrichtigung." und dem Zusammenfassungstext "Dies ist der Zusammenfassungstext der Benachrichtigung."]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

Der Zusammenfassungstext wird in der erweiterten Ansicht unter dem Text der Nachricht angezeigt. 

![Eine Android Nachricht mit dem Titel "Dies ist der Titel der Benachrichtigung." und dem Zusammenfassungstext "Dies ist der Zusammenfassungstext der Benachrichtigung."]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Bei Push-Benachrichtigungen, die Bilder enthalten, wird der Nachrichtentext in der eingeklappten Ansicht angezeigt, während der Zusammenfassungstext als Bildunterschrift angezeigt wird, wenn die Benachrichtigung erweitert wird. 

### Benutzerdefinierte URIs {#custom-uri}

Mit der Funktion **Benutzerdefinierte URI** können Sie eine Web-URL oder eine Android-Ressource angeben, zu der navigiert werden soll, wenn die Benachrichtigung angeklickt wird. Wenn kein benutzerdefinierter URI angegeben ist, gelangen Benutzer durch Klicken auf die Benachrichtigung zu Ihrer App. Sie können die angepasste URI verwenden, um Deeplinks in Ihrer App zu setzen und Nutzer zu Ressourcen außerhalb Ihrer App zu leiten. Dies kann über die [Messaging-API]({{site.baseurl}}/api/endpoints/messaging/) oder unser Dashboard unter **Erweiterte Einstellungen** im Push Composer wie abgebildet festgelegt werden:

![Erweiterte Einstellung für Deeplinking im Braze Push Composer.]({% image_buster /assets/img_archive/deep_link.png %})

### Benachrichtigungs-Anzeigepriorität {#notification-priority}

{% alert important %}
Die Einstellung für die Priorität der Benachrichtigungsanzeige wird auf Geräten mit Android O oder neuer nicht mehr verwendet. Bei neueren Geräten legen Sie die Priorität über die [Konfiguration des Benachrichtigungskanals](https://developer.android.com/training/notify-user/channels#importance) fest.
{% endalert %}

Die Prioritätsstufe einer Push-Benachrichtigung wirkt sich darauf aus, wie Ihre Benachrichtigung im Vergleich zu anderen Benachrichtigungen in der Benachrichtigungsleiste angezeigt wird. Dies kann sich auch auf die Geschwindigkeit und die Art der Zustellung auswirken, da normale Nachrichten und Nachrichten mit geringerer Priorität mit etwas höherer Latenz oder in Stapeln gesendet werden, um den Akku zu schonen, während Nachrichten mit hoher Priorität immer sofort gesendet werden.

In Android O wurde die Benachrichtigungspriorität eine Eigenschaft der Benachrichtigungskanäle. Sie müssen mit Ihrem Entwickler zusammenarbeiten, um die Priorität für einen Kanal während seiner Konfiguration festzulegen und dann das Dashboard verwenden, um den richtigen Kanal auszuwählen, wenn Sie Ihre Benachrichtigungstöne senden. Für Geräte, auf denen Android-Versionen vor O laufen, können Sie über das Braze-Dashboard und die Messaging API eine Prioritätsstufe für Android-Benachrichtigungen festlegen. 

Um Ihrer gesamten Nutzerbasis Nachrichten mit einer bestimmten Priorität zukommen zu lassen, empfehlen wir Ihnen, die Priorität indirekt über die [Konfiguration des Messaging-Kanals](https://developer.android.com/training/notify-user/channels#importance) festzulegen (um O+ Geräte zu targetieren) *und* die individuelle Priorität über das Dashboard zu senden (um <O Geräte zu targetieren).

Die Prioritätsstufen, die Sie bei Push-Benachrichtigungen für Android oder Fire OS einstellen können, sind:

| Priorität | Beschreibung/Verwendungszweck | `priority` Wert (für API-Nachrichten) |
|----------|--------------------------|-------------------------------------|
| Max.      | Dringende oder zeitkritische Nachrichten | `2` |
| Hoch     | Wichtige Mitteilungen, wie z.B. eine neue Nachricht von einem Freund | `1` |
| Standard  | Die meisten Benachrichtigungen - verwenden Sie diese Option, wenn Ihre Nachricht nicht ausdrücklich unter eine der anderen Prioritätsarten fällt. | `0` |
| Niedrig      | Informationen, die Sie Ihren Nutzern mitteilen möchten, die aber keine sofortige Aktion erfordern | `-1` |
| Min.      | Kontextuelle oder Hintergrundinformationen. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Weitere Informationen finden Sie in der Dokumentation zu [den Android-Benachrichtigungen](http://developer.android.com/design/patterns/notifications.html) von Google.

### Töne {#sounds}

In Android O wurden die Benachrichtigungstöne eine Eigenschaft der Benachrichtigungskanäle. Sie müssen mit Ihrem Entwickler zusammenarbeiten, um den Ton für einen Kanal während seiner Konfiguration zu definieren und dann das Dashboard verwenden, um den richtigen Kanal auszuwählen, wenn Sie Ihre Benachrichtigungen senden.

Für Geräte mit Android-Versionen vor O können Sie mit Braze den Ton einer einzelnen Push-Nachricht über den Dashboard Composer einstellen. Hierzu können Sie eine lokale Tonressource auf dem Gerät angeben (z. B. `android.resource://com.mycompany.myapp/raw/mysound`). Wenn Sie in diesem Feld "default" angeben, wird der standardmäßige Benachrichtigungston auf dem Gerät abgespielt. Dies kann über die [Messaging API]({{site.baseurl}}/api/endpoints/messaging/) oder das Dashboard unter **Erweiterte Einstellungen** im Push-Composer festgelegt werden.

![Erweiterte Einstellung für Töne im Braze Push Composer.]({% image_buster /assets/img_archive/sound_android.png %})

Geben Sie die vollständige URI der Tonressource (z. B. `android.resource://com.mycompany.myapp/raw/mysound`) in die Eingabeaufforderung des Dashboards ein.

Um Ihre gesamte Nutzerbasis mit einem bestimmten Ton zu benachrichtigen, empfehlen wir Ihnen, den Ton indirekt über die [Konfiguration des Benachrichtigungskanals](https://developer.android.com/training/notify-user/channels) festzulegen (um O+ Geräte zu targetieren) *und* den individuellen Ton über das Dashboard zu senden (um <O Geräte zu targetieren).
