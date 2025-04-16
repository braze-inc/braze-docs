---
nav_title: Push-Primer-In-App-Nachrichten
article_title: Push-Primer-In-App-Nachrichten
page_order: 1
page_type: reference
description: "In diesem Artikel erfahren Sie, welche Voraussetzungen für Push-Primer-In-App-Nachrichten erfüllt sein müssen und wie Sie sie einrichten können."
channel: push

---

# Push Primer In-App Nachrichten

![Push-Primer-In-App-Nachricht für die Streaming-App. Die Benachrichtigung lautet "Erhalten Sie Push-Benachrichtigungen von Movie Cannon? Die Benachrichtigungen können neue Filme, Fernsehsendungen oder andere Hinweise enthalten und können jederzeit ausgeschaltet werden."][1]{: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Sie haben nur eine Chance, die Nutzer um ihre Zustimmung zu Push-Nachrichten zu bitten. Daher ist die Optimierung Ihrer Push-Registrierung entscheidend, um die Reichweite Ihrer Push-Nachrichten zu maximieren. Um dies zu erreichen, können Sie In-App-Nachrichten verwenden, um zu erklären, welche Art von Nachrichten Ihre Nutzer:innen erwarten können, wenn sie sich für die Teilnahme entscheiden, bevor Sie ihnen der native Push-Prompt zeigen. Dies wird als „Push Primer“ bezeichnet.

Um eine Push-Primer-In-App-Nachricht in Braze zu erstellen, können Sie beim Erstellen einer In-App-Nachricht für iOS, Android oder Web das On-Click-Verhalten „Push-Berechtigung anfordern“ verwenden.

## Voraussetzungen

Dieser Leitfaden verwendet den Button [On-Click-Verhalten](#button-actions), der nur von neueren SDK-Versionen unterstützt wird. Beachten Sie, dass einige dieser SDKs möglicherweise noch nicht veröffentlicht sind. Besuchen Sie die folgenden Links, um die aktuelle Version zu überprüfen:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### Hinweise für Entwicklungsteams

#### Android

- **Android 12 und früher:** Die Push-Primer-Implementierung wird nicht empfohlen, da Push standardmäßig aktiviert ist.
- **Android 13 und höher:** Wenn Sie den Prompt während des Tests mehrmals sehen möchten, gehen Sie in die Geräteeinstellungen und deaktivieren Sie Push für die App, damit der Primer erneut angezeigt werden kann.

#### iOS

- Der iOS-Prompt kann nur einmal pro Installation angezeigt werden, was durch das Betriebssystem erzwungen wird.
- Die Aufforderung wird nicht angezeigt, wenn die Push-Einstellung der App explizit ein- oder ausgeschaltet ist, sondern nur für Benutzer mit [vorläufiger Autorisierung](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - Wenn wir feststellen, dass die Push-Einstellung der App aktiviert ist, zeigt Braze die In-App-Nachricht nicht an, da der oder die Nutzer:in bereits eingewilligt hat.
  - Wenn die Push-Einstellung der App deaktiviert ist, sollten Sie den Benutzer zu den Benachrichtigungseinstellungen der App in der Einstellungs-App weiterleiten.

##### Entfernung von manuellem Code

Die In-App-Nachricht, die Sie mit Hilfe dieses Tutorials eingerichtet haben, ruft automatisch den nativen Push-Prompt-Code auf, wenn ein:e Nutzer:in auf den Button für die In-App-Nachricht klickt. Um zu vermeiden, dass die Erlaubnis für Push-Benachrichtigungen zweimal oder zum falschen Zeitpunkt angefordert wird, sollte ein Entwickler die von ihm implementierte Integration von Push-Benachrichtigungen ändern, um sicherzustellen, dass Ihre In-App-Nachricht die erste Push-Benachrichtigung ist, die Ihre Benutzer sehen.

Der Entwickler sollte seine Implementierung von Push-Benachrichtigungen für Ihre App oder Website überprüfen und manuell jeglichen Code entfernen, der eine Push-Erlaubnis anfordern würde. Suchen Sie zum Beispiel nach Verweisen auf den folgenden Code und entfernen Sie diese:

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
requestAuthorizationWithOptions
```
{% endtab %}
{% tab schnell %}
```swift
requestAuthorization
```
{% endtab %}
{% tab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endtab %}
{% tab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endtab %}
{% endtabs %}

## Schritt 1: In-App-Nachricht erstellen

[Erstellen Sie eine In-App-Nachricht][2] wie gewohnt.

Wählen Sie einen Nachrichtentyp und ein Layout aus. Damit Sie genügend Platz haben, um zu erklären, welche Push-Benachrichtigungen Ihre Benutzer erwarten können (und um Schaltflächen zu ermöglichen), schlägt Braze entweder eine Vollbild- oder eine modale Nachricht vor. Beachten Sie, dass für eine In-App-Nachricht im Vollbildmodus ein Bild erforderlich ist. 

## Schritt 2: Nachricht erstellen

Jetzt ist es an der Zeit, Ihre Kopie hinzuzufügen! Denken Sie daran, dass ein Push-Primer den Nutzer dazu bringen soll, Push-Benachrichtigungen zu aktivieren. Wir empfehlen Ihnen, in Ihrer Nachricht die Gründe hervorzuheben, warum Ihre Nutzer:innen Push-Benachrichtigungen aktiviert haben sollten. Legen Sie genau fest, welche Art von Benachrichtigungen Sie versenden möchten und welchen Wert diese haben.

Eine Nachrichten-App könnte zum Beispiel den folgenden Push-Primer verwenden:

> Aktuelle Nachrichten zum Mitnehmen! Aktivieren Sie Push-Benachrichtigungen, um Benachrichtigungen über wichtige Geschichten und Themen zu erhalten, die für Sie wichtig sind.

Während eine Streaming-App Folgendes verwenden könnte:

> Erhalten Sie Push-Benachrichtigungen von Movie Cannon? Die Benachrichtigungen können neue Filme, Fernsehsendungen oder andere Hinweise enthalten und können jederzeit ausgeschaltet werden.

Best Practices und zusätzliche Ressourcen finden Sie unter [Erstellen von angepassten Opt-in-Prompts][3].

## Schritt 3: Button-Verhalten festlegen {#button-actions}

Um Ihrer In-App-Nachricht Schaltflächen hinzuzufügen, fügen Sie Text in die Textfelder **Schaltfläche 1** und **Schaltfläche 2** ein, die die sekundäre bzw. primäre Schaltfläche in Ihrer In-App-Nachricht darstellen. Wir empfehlen „Benachrichtigungen zulassen“ und „Nicht jetzt“ als Start-Buttons, aber es gibt viele verschiedene Button-Prompts, die Sie zuweisen können.

Nachdem Sie eine Button-Kopie hinzugefügt haben, legen Sie für jeden Button das Verhalten beim Anklicken fest:

- **Button 1:** Legen Sie diesen Button auf „Nachricht schließen“ fest. Dies ist Ihr zweiter Button oder die Option „Nicht jetzt“.
- **Button 2:** Legen Sie diesen Button auf „Push-Berechtigung anfordern“ fest. Dies ist Ihr primärer Button oder die Option „Benachrichtigungen zulassen“.

![][4]

## Schritt 4: Zeitplan für Zustellung

Um Ihren Push-Primer so einzustellen, dass er zu einem bestimmten Zeitpunkt versendet wird, müssen Sie Ihre In-App-Nachricht als aktionsbasierte Nachricht mit **Angepasstes Event durchführen** als triggernde Aktion planen.

Auch wenn der ideale Zeitpunkt variiert, empfiehlt Braze, zu warten, bis ein Benutzer eine [hochwertige Aktion](https://www.braze.com/resources/videos/mapping-high-value-actions) durchgeführt hat, die anzeigt, dass er einen Nutzen in Ihrer App oder Website sieht, oder wenn es ein zwingendes Bedürfnis gibt, das durch Push-Benachrichtigungen erfüllt werden kann (z. B. nachdem der Benutzer eine Bestellung aufgegeben hat und Sie ihm Informationen zur Sendungsverfolgung anbieten möchten). Auf diese Weise ist die Aufforderung nicht nur für Ihre Marke, sondern auch für den Kunden von Vorteil.

![][5]

## Schritt 5: Zielnutzer:innen

Da das Ziel einer Push-Primer-Kampagne darin besteht, Nutzer dazu zu bewegen, sich für Push-Nachrichten zu entscheiden, sollten Sie keine Nutzer ansprechen, die sich bereits für Push-Nachrichten entschieden haben. Fügen Sie dazu ein Segment oder einen Filter hinzu, bei dem `Push Subscription Status is not Opted In`.

Darüber hinaus können Sie entscheiden, welche zusätzlichen Segmente Sie für sinnvoll halten. So könnten Sie beispielsweise Nutzer ansprechen, die einen zweiten Kauf getätigt haben, Nutzer, die gerade ein Konto erstellt haben, um Mitglied zu werden, oder sogar Nutzer, die Ihre App mehr als zweimal pro Woche besuchen. Die gezielte Ansprache von Nutzern in diesen wichtigen Segmenten erhöht die Wahrscheinlichkeit, dass sich die Nutzer für die Push-Funktion entscheiden und diese aktivieren.

## Schritt 6: Konversions-Events

Braze schlägt Standardeinstellungen für Konvertierungen vor, aber vielleicht möchten Sie [Konvertierungsereignisse]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) für Push-Primer einrichten.

[1]: {% image_buster /assets/img_archive/push_primer_iam.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/creating_custom_opt-in_prompts/
[4]: {% image_buster /assets/img_archive/push_primer_button_behavior.png %}
[5]: {% image_buster /assets/img_archive/push_primer_trigger.png %}
