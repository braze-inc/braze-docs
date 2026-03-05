---
nav_title: Push Primer In-App Nachrichten
article_title: Push-Primer-In-App-Nachrichten
page_order: 1
page_type: reference
description: "In diesem Artikel erfahren Sie, welche Voraussetzungen für Push-Primer-In-App-Nachrichten erfüllt sein müssen und wie Sie sie einrichten können."
channel: push

---

# Push Primer In-App Nachrichten

![Push-Primer-In-App-Nachricht für die Streaming-App. Die Benachrichtigung lautet "Erhalten Sie Push-Benachrichtigungen von Movie Cannon? Die Benachrichtigungen können neue Filme, Fernsehsendungen oder andere Hinweise enthalten und können jederzeit ausgeschaltet werden."]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Sie haben nur eine Chance, die Nutzer um ihre Zustimmung zu Push-Nachrichten zu bitten. Daher ist die Optimierung Ihrer Push-Registrierung entscheidend, um die Reichweite Ihrer Push-Nachrichten zu maximieren. Um dies zu erreichen, können Sie In-App-Nachrichten verwenden, um zu erklären, welche Art von Nachrichten Ihre Nutzer:innen erwarten können, wenn sie sich für die Teilnahme entscheiden, bevor Sie ihnen der native Push-Prompt zeigen. Dies wird als „Push Primer“ bezeichnet.

Um eine Push-Primer-In-App-Nachricht in Braze zu erstellen, können Sie beim Erstellen einer In-App-Nachricht für iOS, Android oder Web das On-Click-Verhalten „Push-Berechtigung anfordern“ verwenden.

## Voraussetzungen

Dieses Feature erfordert das [Verhalten von Buttons beim Klicken](#button-actions), das in den folgenden Mindestversionen oder höher unterstützt wird:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Beachten Sie außerdem die folgenden plattformspezifischen Details:

{% tabs local %}
{% tab android %}
|OS-Version|Zusätzliche Informationen|
\|----------|----------------------|
| **Android 12 und früher** | Die Implementierung von Push-Primern wird nicht empfohlen, da Push standardmäßig Opt-in ist. |
| **Android 13+** | Wenn ein Nutzer:innen Ihre Push-Erlaubnis zweimal verweigert, blockiert Android weitere Aufforderungen - einschließlich der Push-Nachrichten von Braze. Um die Erlaubnis danach zu erteilen, müssen Nutzer:innen Push für Ihre App in ihren Geräteeinstellungen manuell aktivieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab swift %}
### Allgemeine Informationen

- Die Push-Eingabeaufforderung kann nur einmal pro Installation angezeigt werden, was durch das Betriebssystem erzwungen wird.
- Die Aufforderung wird nicht angezeigt, wenn die Push-Einstellung der App explizit ein- oder ausgeschaltet ist. Es wird nur für Nutzer:innen mit [vorläufiger Berechtigung](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375) angezeigt.
  - **Die Push-Einstellung der App ist aktiviert:** Braze zeigt die In-App-Nachricht nicht an, da der Nutzer:in bereits ein Opt-in vorgenommen hat.
  - **Die Push-Einstellung der App ist ausgeschaltet:** Sie müssen den Nutzer:innen in den Geräteeinstellungen zu den Einstellungen für Push-Benachrichtigungen Ihrer App weiterleiten.

### Entfernung von manuellem Code

Die In-App-Nachricht, die Sie mit Hilfe dieses Tutorials einrichten, ruft automatisch den nativen Code für die Push-Aufforderung auf, wenn ein Nutzer:in auf den Button für die In-App-Nachricht klickt. Um zu vermeiden, dass die Erlaubnis für Push-Benachrichtigungen zweimal oder zum falschen Zeitpunkt angefordert wird, sollte ein Entwickler die von ihm implementierte Integration von Push-Benachrichtigungen ändern, um sicherzustellen, dass Ihre In-App-Nachricht die erste Push-Benachrichtigung ist, die Ihre Benutzer sehen.

Ihr Entwickler:in Team sollte die Implementierung von Push-Benachrichtigungen für Ihre App oder Website überprüfen und jeden Code, der eine Push-Erlaubnis anfragt, manuell entfernen. Entfernen Sie zum Beispiel Referenzen auf den folgenden Code:

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
requestAuthorizationWithOptions
```
{% endsubtab %}
{% subtab swift %}
```swift
requestAuthorization
```
{% endsubtab %}
{% subtab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endsubtab %}
{% subtab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Schritt 1: In-App-Nachricht erstellen

[Erstellen Sie zunächst eine In-App-Nachricht]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) und wählen Sie dann den Typ und das Layout Ihrer Nachricht aus.

Um sicherzustellen, dass Sie genügend Platz für Ihre Nachrichten und Buttons haben, verwenden Sie ein Vollbild- oder modales Nachrichtenlayout. Wenn Sie den Vollbildmodus wählen, beachten Sie, dass ein Bild erforderlich ist.

## Schritt 2: Nachricht erstellen

Jetzt ist es an der Zeit, Ihre Kopie hinzuzufügen! Denken Sie daran, dass ein Push-Primer den Nutzer dazu bringen soll, Push-Benachrichtigungen zu aktivieren. Wir empfehlen Ihnen, in Ihrer Nachricht die Gründe hervorzuheben, warum Ihre Nutzer:innen Push-Benachrichtigungen aktiviert haben sollten. Legen Sie genau fest, welche Art von Benachrichtigungen Sie versenden möchten und welchen Wert diese haben.

Eine Nachrichten-App könnte zum Beispiel den folgenden Push-Primer verwenden:

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

Während eine Streaming-App Folgendes verwenden könnte:

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

Bewährte Verfahren und zusätzliche Ressourcen finden Sie unter [Erstellen angepasster Opt-in-Anfragen]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Schritt 3: Button-Verhalten festlegen {#button-actions}

Um Buttons zu Ihrer In-App-Nachricht hinzuzufügen, ziehen Sie zwei **Button-Blöcke** in Ihre Nachricht, die als primäre und sekundäre Buttons in Ihrer In-App-Nachricht fungieren. Sie können auch eine Zeile in Ihre Nachricht ziehen und dann die Buttons in die Zeile ziehen, so dass die Buttons in der gleichen horizontalen Zeile stehen (und nicht übereinander gestapelt sind). Wir empfehlen "Benachrichtigungen zulassen" und "Nicht jetzt" als Start-Buttons, aber es gibt viele verschiedene Button-Aufforderungen, die Sie zuweisen können.

Nachdem Sie eine Button-Kopie hinzugefügt haben, legen Sie für jeden Button das Verhalten beim Anklicken fest:

- **Button 1:** Legen Sie diesen Button auf „Nachricht schließen“ fest. Dies ist Ihr zweiter Button oder die Option „Nicht jetzt“.
- **Button 2:** Legen Sie diesen Button auf „Push-Berechtigung anfordern“ fest. Dies ist Ihr primärer Button oder die Option „Benachrichtigungen zulassen“.

![In-App-Nachricht-Editor mit zwei Buttons: "Benachrichtigungen zulassen" und "Nicht jetzt".]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Schritt 4: Zeitplan für Zustellung

Um Ihren Push-Primer so einzustellen, dass er zu einem bestimmten Zeitpunkt versendet wird, müssen Sie Ihre In-App-Nachricht als aktionsbasierte Nachricht mit **Angepasstes Event durchführen** als triggernde Aktion planen.

Auch wenn der ideale Zeitpunkt variiert, empfiehlt Braze, zu warten, bis ein Benutzer eine [hochwertige Aktion](https://www.braze.com/resources/videos/mapping-high-value-actions) durchgeführt hat, die anzeigt, dass er einen Nutzen in Ihrer App oder Website sieht, oder wenn es ein zwingendes Bedürfnis gibt, das durch Push-Benachrichtigungen erfüllt werden kann (z. B. nachdem der Benutzer eine Bestellung aufgegeben hat und Sie ihm Informationen zur Sendungsverfolgung anbieten möchten). Auf diese Weise ist die Aufforderung nicht nur für Ihre Marke, sondern auch für den Kunden von Vorteil.

![Aktionsbasierte Zustellung für Nutzer:innen, die das angepasste Event "Zur Beobachtungsliste hinzufügen" ausgeführt haben.]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Schritt 5: Zielnutzer:innen

Das Ziel einer Push-Primer Kampagne ist es, Nutzer:innen auf Geräten, für die sie noch keine Push-Berechtigungen erteilt haben, aufzufordern. Das können erstmalige Nutzer:innen oder bestehende Nutzer:innen sein, die ein neues Gerät erhalten oder Ihre Anwendung neu installieren.

{% alert important %}
**Automatische Unterdrückung mit No-Code Push Primer**: Wenn Sie den Push-Primer ohne Code (die Button-Aktion "Push-Erlaubnis anfordern") verwenden, müssen Sie Ihrer Segmentierung keine Filter für Push-Abos hinzufügen. Das SDK unterdrückt automatisch die In-App-Nachricht auf Geräten, die bereits einen aktiven Push-Token haben, unabhängig vom Push-Status des Nutzers auf anderen Geräten. Weitere Informationen zum Targeting von Nutzern:innen mit mehreren Geräten finden Sie unter [Targeting von Nutzern:innen mit mehreren Geräten](#targeting-users-with-multiple-devices).
{% endalert %}

Wenn Sie den Push-Primer ohne Code nicht verwenden, fügen Sie einen Filter hinzu, bei dem `Foreground Push Enabled For App is false`. Dieser Filter identifiziert einzelne App-Installationen, die noch nicht für Push-Benachrichtigungen im Vordergrund opt-in sind.

{% alert important %}
Die Verwendung eines Filters auf Benutzerebene wie `Push Subscription Status is not Opted In` schließt Nutzer:innen aus, die bereits auf einem anderen Gerät ein Opt-in haben, und verhindert, dass sie die Aufforderung auf ihrem neuen Gerät erhalten.
{% endalert %}

Darüber hinaus können Sie entscheiden, welche zusätzlichen Segmente Sie für sinnvoll halten. So könnten Sie beispielsweise Nutzer ansprechen, die einen zweiten Kauf getätigt haben, Nutzer, die gerade ein Konto erstellt haben, um Mitglied zu werden, oder sogar Nutzer, die Ihre App mehr als zweimal pro Woche besuchen. Die gezielte Ansprache von Nutzern in diesen wichtigen Segmenten erhöht die Wahrscheinlichkeit, dass sich die Nutzer für die Push-Funktion entscheiden und diese aktivieren.

### Targeting von Nutzer:innen mit mehreren Geräten

Da Braze Nutzerdaten auf Profilebene und nicht auf Geräteebene erfasst, kann das Targeting von Nutzer:innen, die mehrere Geräte besitzen, eine Herausforderung darstellen. Push-Filter für Abonnements in der Segmentierung schließen Nutzer:innen auf der Grundlage des Abonnementstatus eines einzelnen Geräts ein oder aus und nicht auf der Grundlage des Abonnementstatus des spezifischen Zielgeräts. Darüber hinaus sorgen provisorische Zustände auf iOS für zusätzliche Komplexität, da diese Geräte technisch gesehen zwar über Push-Token für den Vordergrund verfügen, die Nutzer:innen aber nicht explizit opt-in sind.

#### Das Problem mit Push Abo Filtern

Wenn ein Nutzer über mehrere Geräte mit unterschiedlichen Push-Abonnement-Status verfügt, können die Push-Abonnement-Filter in Ihrer Segmentierung einige Nutzer:innen nicht gezielt ansprechen. Betrachten Sie diese Szenarien:

{% details Scenario 1: User has two devices on different platforms %}

**Nutzer:innen haben zwei Geräte:**
- Gerät A: Android, Opt-in für Push
- Gerät B: iOS, kein Opt-in für Push

**Segmentierte Filter, die nicht funktionieren:**
- `Push enabled = false` - Nutzer:innen haben auf ihrem Android Gerät Push Enablement, so dass sie nicht in das Segment fallen. Das Segment beinhaltet nicht das iOS Gerät.
- `Push subscription status is not opted in` - Nutzer:innen haben auf ihrem Android Gerät Push Enablement, so dass sie nicht in das Segment fallen. Das Segment beinhaltet nicht das iOS Gerät.

**Segmentierte Filter, die funktionieren:**
- `Push enabled for iOS = false` - Der Nutzer ist auf seinem Android Gerät für Push aktiviert, aber wir targeting nur iOS Geräte, also fällt der Nutzer:innen in das Segment. Das Segment umfasst das iOS Gerät.

{% enddetails %}

{% details Scenario 2: User has two iOS devices with different states %}

**Nutzer:innen haben zwei iOS Geräte:**
- Gerät A: Opt-in für Push
- Gerät B: Provisorisch Enablement, aber kein Opt-in

**Segmentierte Filter, die nicht funktionieren:**
- `Push enabled = false` - Gerät A hat ein Opt-in für Push, so dass der Nutzer:innen nicht in das Segment fällt. Das Segment enthält nicht das Gerät B.
- `Provisionally opted in = true` - Gerät A ist vollständig Opt-in, d.h. es befindet sich nicht in einem provisorischen Zustand. Der Nutzer:innen fällt nicht in das Segment. Das Segment enthält nicht das Gerät B.
- `Push enabled for app > iOS = false` - Gerät A hat ein Opt-in für Push auf iOS, also fällt der Nutzer:in nicht in das Segment. Das Segment enthält nicht das Gerät B.
- `Push subscription status is not opted in` - Gerät A hat ein Opt-in für Push, so dass der Nutzer:innen nicht in das Segment fällt. Das Segment enthält nicht das Gerät B.

**Ergebnis:** Die Verwendung einer beliebigen Kombination dieser Push-Filter führt dazu, dass das Segment mindestens ein Gerät ausschließt.

{% enddetails %}

{% details Scenario 3: User has three or more devices on the same OS %}

**Nutzer:innen haben drei Geräte:**
- Gerät A: Opt-in für Push
- Gerät B: Nicht für Push opt-in
- Gerät C: Nicht für Push opt-in

**Segmentierte Filter, die nicht funktionieren:**
- `Push enabled = false` - Gerät A hat ein Opt-in für Push, so dass der Nutzer:innen nicht in das Segment fällt. Das Segment umfasst nicht die Geräte B und C.
- `Push enabled for app > X = false` - Gerät A ist für Push in der angegebenen App opt-in, so dass der Nutzer:in nicht in das Segment fällt. Das Segment umfasst nicht die Geräte B und C.
- `Push subscription status is not opted in` - Gerät A hat ein Opt-in für Push, so dass der Nutzer:innen nicht in das Segment fällt. Das Segment umfasst nicht die Geräte B und C.

**Ergebnis:** Wenn Sie eine beliebige Kombination dieser Push-Filter verwenden, bleibt mindestens ein Gerät unberücksichtigt.

{% enddetails %}

#### Lösung: Verwenden Sie die Push-Fibel ohne Code

Die empfohlene Lösung ist die Verwendung des Push-Primers ohne Code (die Button-Aktion "Push-Erlaubnis anfordern") ohne zusätzliche Filter für die Segmentierung des Push-Status.

{% alert important %}
**Automatische Unterdrückung**: Der No-Code-Push-Primer wird automatisch auf Geräten unterdrückt, die bereits einen aktiven Push-Token haben. Das SDK prüft, ob ein Nutzer:innen auf seinem Gerät bereits ein Push-Token besitzt. Wenn das SDK feststellt, dass der Nutzer:in bereits ein Opt-in gemacht hat (z.B. durch eine frühere Anfrage oder über die Geräteeinstellungen), unterdrückt das SDK automatisch die In-App-Nachricht, ohne dass zusätzliche Segmentierungsfilter erforderlich sind. Die Grundierung wird in allen anderen Szenarien angezeigt, auch wenn ein Nutzer:in vorläufig für Push optiert ist.
{% endalert %}

Der Vorteil der Verwendung des No-Code Push Primers ist, dass die Funktionalität vom Braze SDK unterstützt wird. Da das SDK den Push-Token-Status auf dem spezifischen Gerät, das die Nachricht anzeigt, erkennen kann, sind Sie nicht auf Segmentierungsfilter auf Profilebene angewiesen, die Nutzer:innen mit mehreren Geräten ausschließen können.

#### Überlegungen

**Push-Primer ohne Code erforderlich**: Sie müssen den Push-Primer ohne Code verwenden, damit die automatische Unterdrückung funktioniert. Wenn Sie eine angepasste Logik oder Deeplinks setzen, anstatt die Button-Aktion "Push-Erlaubnis anfordern" zu verwenden, kann das SDK nicht erkennen, dass Sie versuchen, einen Push-Primer anzuzeigen. Dies führt dazu, dass die Nachricht unabhängig vom Status des Abos dieses Geräts angezeigt wird.

**Unterdrückung für Nutzer:in, die sich abgemeldet haben**: Möglicherweise möchten Sie die In-App-Nachricht für Nutzer:innen, die sich explizit gegen Push entschieden haben (z.B. über die native Anfrage oder die Geräteeinstellungen), unterdrücken und diese Nutzer:innen mit einer separaten Retargeting-Kampagne erneut ansprechen. Verwenden Sie dazu die folgende Logik von Liquid in Kombination mit der No-Code-Fibel:

{% raw %}
```liquid
{% if targeted_device.${foreground_push_enabled} == false %} 
{% abort_message('user turned off push notifications') %} 
{% endif %}
- message goes here -
```
{% endraw %}

Der Filter `targeted_device` Liquid betrachtet nur das Gerät, auf dem die Nachricht angezeigt wird, und nicht das Profil des Nutzers:innen. Auf diesem Gerät wird `foreground_push_enabled` auf `true` gesetzt, wenn es ein aktives Push-Token im Vordergrund gibt, und auf `false`, wenn das Betriebssystem meldet, dass Push-Benachrichtigungen deaktiviert wurden (z.B. weil der Nutzer:innen sie ausdrücklich ausgeschaltet hat). Bei völlig neuen Geräten, die noch nicht auf einen Push-Erlaubnisstatus reagiert haben, ist `foreground_push_enabled` nicht gesetzt und hat keinen Wert. Da die Liquid-Bedingung speziell auf `{% raw %}``false`{% endraw %} prüft, unterdrückt sie den Primer nur für Geräte mit einem expliziten Opt-out, während Geräte in diesem unbekannten Zustand weiterhin qualifiziert sind und den Push-Primer empfangen können.

## Schritt 6: Konversions-Events

Braze schlägt Standardeinstellungen für Konvertierungen vor, aber vielleicht möchten Sie [Konvertierungsereignisse]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) für Push-Primer einrichten.