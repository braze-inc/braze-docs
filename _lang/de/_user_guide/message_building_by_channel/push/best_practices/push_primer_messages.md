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
- Die Eingabeaufforderung wird nicht angezeigt, wenn die Push-Einstellung der App explizit aktiviert oder deaktiviert ist. Es wird nur für Nutzer:innen mit [vorläufiger Berechtigung](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375) angezeigt.
  - **Die Push-Einstellung der App ist aktiviert:** Braze zeigt die In-App-Nachricht nicht an, da der Nutzer:in bereits zum Opt-in zugestimmt hat.
  - **Die Push-Einstellung der App ist ausgeschaltet:** Bitte leiten Sie den Nutzer:in in den Einstellungen des Geräts zu den Einstellungen der Push-Benachrichtigung Ihrer App weiter.

### Entfernung von manuellem Code

Die In-App-Nachricht, die Sie mithilfe dieses Tutorials eingerichtet haben, ruft automatisch den nativen Push-Prompt-Code auf, wenn ein Nutzer:in auf den Button für In-App-Nachrichten klickt. Um zu vermeiden, dass die Erlaubnis für Push-Benachrichtigungen zweimal oder zum falschen Zeitpunkt angefordert wird, sollte ein Entwickler die von ihm implementierte Integration von Push-Benachrichtigungen ändern, um sicherzustellen, dass Ihre In-App-Nachricht die erste Push-Benachrichtigung ist, die Ihre Benutzer sehen.

Ihr Entwicklungsteam sollte die Implementierung von Push-Benachrichtigungen für Ihre App oder Website überprüfen und jeglichen Code, der eine Anfrage für eine Push-Berechtigung stellt, manuell entfernen. Bitte entfernen Sie beispielsweise Verweise auf den folgenden Code:

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

Um Ihrer In-App-Nachricht Schaltflächen hinzuzufügen, ziehen Sie bitte zwei Schaltflächenblöcke in Ihre Nachricht, die als primäre und sekundäre Schaltflächen in Ihrer In-App-Nachricht fungieren. Sie können auch eine Zeile in Ihre Nachricht ziehen und dann die Buttons in die Zeile ziehen, so dass die Buttons in der gleichen horizontalen Zeile stehen (und nicht übereinander gestapelt sind). Wir empfehlen „Benachrichtigungen zulassen“ und „Nicht jetzt“ als Start-Buttons, jedoch stehen Ihnen zahlreiche verschiedene Buttons zur Auswahl.

Nachdem Sie eine Button-Kopie hinzugefügt haben, legen Sie für jeden Button das Verhalten beim Anklicken fest:

- **Button 1:** Legen Sie diesen Button auf „Nachricht schließen“ fest. Dies ist Ihr zweiter Button oder die Option „Nicht jetzt“.
- **Button 2:** Legen Sie diesen Button auf „Push-Berechtigung anfordern“ fest. Dies ist Ihr primärer Button oder die Option „Benachrichtigungen zulassen“.

![In-App-Nachricht-Editor mit zwei Buttons: „Benachrichtigungen zulassen“ und „Nicht jetzt“.]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Schritt 4: Zeitplan für Zustellung

Um Ihren Push-Primer so einzustellen, dass er zu einem bestimmten Zeitpunkt versendet wird, müssen Sie Ihre In-App-Nachricht als aktionsbasierte Nachricht mit **Angepasstes Event durchführen** als triggernde Aktion planen.

Auch wenn der ideale Zeitpunkt variiert, empfiehlt Braze, zu warten, bis ein Benutzer eine [hochwertige Aktion](https://www.braze.com/resources/videos/mapping-high-value-actions) durchgeführt hat, die anzeigt, dass er einen Nutzen in Ihrer App oder Website sieht, oder wenn es ein zwingendes Bedürfnis gibt, das durch Push-Benachrichtigungen erfüllt werden kann (z. B. nachdem der Benutzer eine Bestellung aufgegeben hat und Sie ihm Informationen zur Sendungsverfolgung anbieten möchten). Auf diese Weise ist die Aufforderung nicht nur für Ihre Marke, sondern auch für den Kunden von Vorteil.

![Aktionsbasierte Zustellung für den Versand an Nutzer:innen, die das angepasste Event „Zur Beobachtungsliste hinzufügen” ausgeführt haben.]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Schritt 5: Zielnutzer:innen

Das Ziel einer Push-Primer-Kampagne besteht darin, Nutzer:innen auf allen Geräten, auf denen sie noch keine Push-Berechtigungen erteilt haben, dazu aufzufordern, diese zu erteilen. Dies kann Erstnutzer:innen oder bestehende Nutzer:innen umfassen, die ein neues Gerät erwerben oder Ihre Anwendung neu installieren.

{% alert important %}
**Automatische Unterdrückung mit No-Code-Push-Primer**: Wenn Sie die No-Code-Push-Einführung verwenden (der Button „Push-Berechtigung anfordern“), müssen Sie Ihrer Segmentierung keine Push-Abo-Filter hinzufügen. Das SDK unterdrückt automatisch die In-App-Nachricht auf Geräten, die bereits über ein aktives Push-Token verfügen, unabhängig vom Push-Status des Nutzers auf anderen Geräten. Weitere Informationen zum Targeting von Nutzern mit mehreren Geräten finden Sie unter [Targeting von Nutzern mit mehreren Geräten](#targeting-users-with-multiple-devices).
{% endalert %}

Falls Sie die No-Code-Push-Einführung nicht verwenden, fügen Sie bitte einen Filter hinzu, wo `Foreground Push Enabled For App is false`. Dieser Filter identifiziert einzelne App-Installationen, die noch nicht für Push-Benachrichtigungen im Vordergrund opt-in sind.

{% alert important %}
Durch die Verwendung eines Filters auf Benutzerebene wie`Push Subscription Status is not Opted In`  werden Nutzer:innen ausgeschlossen, die sich bereits auf einem anderen Gerät angemeldet haben, sodass sie die Opt-in-Anfrage nicht auf ihrem neuen Gerät erhalten.
{% endalert %}

Darüber hinaus können Sie entscheiden, welche zusätzlichen Segmente Sie für sinnvoll halten. So könnten Sie beispielsweise Nutzer ansprechen, die einen zweiten Kauf getätigt haben, Nutzer, die gerade ein Konto erstellt haben, um Mitglied zu werden, oder sogar Nutzer, die Ihre App mehr als zweimal pro Woche besuchen. Die gezielte Ansprache von Nutzern in diesen wichtigen Segmenten erhöht die Wahrscheinlichkeit, dass sich die Nutzer für die Push-Funktion entscheiden und diese aktivieren.

### Targeting von Nutzern mit mehreren Geräten

Da Braze Nutzerdaten auf Profilebene und nicht auf Geräteebene erfasst, kann es schwierig sein, Nutzer:innen zu erreichen, die mehrere Geräte besitzen. Push-Abonnementfilter in der Segmentierung schließen Nutzer:innen auf der Grundlage des Abonnementstatus eines einzelnen Geräts ein oder aus, anstatt auf der Grundlage des Abonnementstatus des spezifischen Zielgeräts. Darüber hinaus erhöhen vorläufige Zustände unter iOS die Komplexität, da diese Geräte technisch über Push-Token im Vordergrund verfügen, aber die Nutzer:innen nicht ausdrücklich für das Opt-in eingestimmt haben.

#### Das Problem mit Push-Abo-Filtern

Wenn ein Nutzer:in über mehrere Geräte mit unterschiedlichen Push-Abo-Status verfügt, können Push-Abo-Filter in seiner Segmentierung möglicherweise einige Geräte nicht ansprechen. Bitte berücksichtigen Sie die folgenden Szenarien:

{% details Scenario 1: User has two devices on different platforms %}

**Die Nutzer:innen verfügen über zwei Geräte:**
- Gerät A: Android, Opt-in für Push-Benachrichtigungen
- Gerät B: iOS, nicht für Push-Benachrichtigungen Opt-in durchgeführt

**Filter, die nicht funktionieren:**
- `Push enabled = false` - Der Nutzer:in hat Push-Benachrichtigungen auf seinem Android-Gerät aktiviert, daher fällt er nicht in dieses Segment. Das Segment umfasst keine iOS-Geräte.
- `Push subscription status is not opted in` - Der Nutzer:in hat Push-Benachrichtigungen auf seinem Android-Gerät aktiviert, daher fällt er nicht in dieses Segment. Das Segment umfasst keine iOS-Geräte.

**Filter, die funktionieren:**
- `Push enabled for iOS = false` - Der Nutzer hat Push-Benachrichtigungen auf seinem Android-Gerät aktiviert, jedoch richten wir uns ausschließlich an iOS-Geräte, daher fällt der Nutzer in das Segment. Das Segment umfasst das iOS-Gerät.

{% enddetails %}

{% details Scenario 2: User has two iOS devices with different states %}

**Die Nutzer:innen verfügen über zwei iOS-Geräte:**
- Gerät A: Für Push-Benachrichtigungen Opt-in
- Gerät B: Vorläufig aktiviert, jedoch nicht Opt-in

**Filter, die nicht funktionieren:**
- `Push enabled = false` - Gerät A ist für Push-Benachrichtigungen im Opt-in-Modus, daher fällt die Nutzer:in nicht in das Segment. Das Segment umfasst nicht Gerät B.
- `Provisionally opted in = true` - Gerät A ist vollständig für das Opt-in aktiviert, was bedeutet, dass es sich nicht in einem vorläufigen Zustand befindet. Der Nutzer:in gehört nicht zu diesem Segment. Das Segment umfasst nicht Gerät B.
- `Push enabled for app > iOS = false` - Gerät A hat ein Opt-in für Push-Benachrichtigungen auf iOS, daher fällt die Nutzer:in nicht in ein Segment. Das Segment umfasst nicht Gerät B.
- `Push subscription status is not opted in` - Gerät A ist für Push-Benachrichtigungen im Opt-in-Modus, daher fällt die Nutzer:in nicht in das Segment. Das Segment umfasst nicht Gerät B.

**Ergebnis:** Die Verwendung einer beliebigen Kombination dieser Push-Filter führt dazu, dass mindestens ein Gerät aus dem Segment ausgeschlossen wird.

{% enddetails %}

{% details Scenario 3: User has three or more devices on the same OS %}

**Die Nutzer:in verfügt über drei Geräte:**
- Gerät A: Für Push-Benachrichtigungen Opt-in
- Gerät B: Nicht für Push-Benachrichtigungen Opt-in durchgeführt
- Gerät C: Nicht für Push-Benachrichtigungen Opt-in durchgeführt

**Filter, die nicht funktionieren:**
- `Push enabled = false` - Gerät A ist für Push-Benachrichtigungen im Opt-in-Modus, daher fällt die Nutzer:in nicht in das Segment. Das Segment umfasst nicht die Geräte B und C.
- `Push enabled for app > X = false` - Gerät A ist für Push-Benachrichtigungen der angegebenen App im Opt-in-Verfahren aktiviert, daher fällt die Nutzer:in nicht in ein Segment. Das Segment umfasst nicht die Geräte B und C.
- `Push subscription status is not opted in` - Gerät A ist für Push-Benachrichtigungen im Opt-in-Modus, daher fällt die Nutzer:in nicht in das Segment. Das Segment umfasst nicht die Geräte B und C.

**Ergebnis:** Bei Verwendung einer beliebigen Kombination dieser Push-Filter bleibt mindestens ein Gerät unberücksichtigt.

{% enddetails %}

#### Lösung: Bitte verwenden Sie die No-Code-Push-Einführung.

Die empfohlene Lösung besteht darin, den No-Code-Push-Primer (der Button „Push-Berechtigung anfordern“) ohne zusätzliche Filter für die Segmentierung des Push-Status zu verwenden.

{% alert important %}
**Automatische Unterdrückung**: Die No-Code-Push-Einführung wird automatisch auf Geräten unterdrückt, die bereits über ein aktives Push-Token verfügen. Das SDK überprüft, ob ein Nutzer:in auf seinem spezifischen Gerät bereits über ein Push-Token verfügt. Wenn das SDK feststellt, dass der Nutzer bereits zum Opt-in zugestimmt hat (z. B. aufgrund einer früheren Anfrage oder über die Geräteeinstellungen), unterdrückt das SDK automatisch die In-App-Nachricht, ohne dass zusätzliche Filter für die Segmentierung erforderlich sind. Die Anleitung zeigt alle anderen Szenarien, einschließlich der Situation, in der eine Nutzer:in vorläufig für Push-Benachrichtigungen opt-in ist.
{% endalert %}

Der Vorteil der Verwendung des No-Code-Push-Primers besteht darin, dass die Funktionalität vom Braze SDK unterstützt wird. Da das SDK den Push-Token-Status auf dem spezifischen Gerät, das die Nachricht anzeigt, erkennen kann, müssen Sie sich nicht auf Segmentierungsfilter auf Profilebene verlassen, die Nutzer:innen mit mehreren Geräten möglicherweise ausschließen.

#### Überlegungen

**Keine Programmierkenntnisse erforderlich für Push**: Bitte beachten Sie, dass Sie die No-Code-Push-Einführung verwenden müssen, damit die automatische Unterdrückung funktioniert. Wenn Sie anstelle der Schaltflächenaktion „Push-Berechtigung anfordern“ eine angepasste Logik oder Deeplinks setzen, kann das SDK nicht erkennen, dass Sie versuchen, einen Push-Primer anzuzeigen. Dies führt dazu, dass die Nachricht unabhängig vom Abo-Status des Geräts angezeigt wird.

**Unterdrückung für Nutzer:innen, die sich abgemeldet haben**: Es kann sinnvoll sein, die In-App-Nachricht für Nutzer:innen zu unterdrücken, die sich ausdrücklich gegen Push-Benachrichtigungen entschieden haben (z. B. über die native Anfrage oder die Geräteeinstellungen), und diese Nutzer:innen mit einer separaten Nurture-Kampagne erneut anzusprechen. Bitte verwenden Sie dazu die folgende Liquid-Logik in Kombination mit der No-Code-Einführung:

{% raw %}
```liquid
{% if targeted_device.${foreground_push_enabled} == false %} 
{% abort_message('user turned off push notifications') %} 
{% endif %}
- message goes here -
```
{% endraw %}

Der`targeted_device`Flüssigkeitsfilter berücksichtigt nur das Gerät, auf dem die Nachricht angezeigt wird, und nicht das Nutzerprofil. Auf diesem Gerät wird  auf  gesetzt`foreground_push_enabled``true`, wenn ein aktives Push-Token im Vordergrund vorhanden ist, und auf  gesetzt`false`, wenn das Betriebssystem meldet, dass Push-Benachrichtigungen deaktiviert wurden (z. B. wenn der Nutzer:in sie explizit ausgeschaltet hat). Bei völlig neuen Geräten, die noch nicht auf einen Push-Berechtigungsstatus reagiert haben,`foreground_push_enabled`ist  nicht gesetzt und hat keinen Wert. Da die Liquid-Bedingung speziell `{% raw %}``false`{% endraw %}nach „opt-out“ sucht, unterdrückt sie den Primer nur für Geräte mit einem expliziten Opt-out, während Geräte in diesem unbekannten Zustand weiterhin qualifiziert sind und den Push-Primer erhalten können.

## Schritt 6: Konversions-Events

Braze schlägt Standardeinstellungen für Konvertierungen vor, aber vielleicht möchten Sie [Konvertierungsereignisse]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) für Push-Primer einrichten.