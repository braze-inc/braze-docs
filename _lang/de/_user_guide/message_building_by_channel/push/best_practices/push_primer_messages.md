---
nav_title: Push Primer In-App Nachrichten
article_title: Push-Primer-In-App-Nachrichten
page_order: 1
page_type: reference
description: "In diesem Artikel erfahren Sie, welche Voraussetzungen für Push-Primer-In-App-Nachrichten erfüllt sein müssen und wie Sie sie einrichten können."
channel: push

---

# Push Primer In-App Nachrichten

![Push Primer In-App-Nachricht für Streaming-App. Die Benachrichtigung lautet "Erhalten Sie Push-Benachrichtigungen von Movie Cannon? Die Benachrichtigungen können neue Filme, Fernsehsendungen oder andere Hinweise enthalten und können jederzeit ausgeschaltet werden."]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

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
- Die Aufforderung wird nicht angezeigt, wenn die Push-Einstellung der App explizit ein- oder ausgeschaltet ist, sondern nur für Benutzer mit [vorläufiger Autorisierung](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **Die Push-Einstellung der App ist aktiviert:** Braze zeigt die In-App-Nachricht nicht an, da der Nutzer:in bereits sein Opt-in gegeben hat.
  - **Die Push-Einstellung der App ist ausgeschaltet:** Sie müssen den Nutzer:innen in den Einstellungen des Geräts zu den Push-Benachrichtigungen Ihrer App weiterleiten.

### Entfernung von manuellem Code

Die In-App-Nachricht, die Sie mit Hilfe dieses Tutorials eingerichtet haben, ruft automatisch den nativen Push-Prompt-Code auf, wenn ein:e Nutzer:in auf den Button für die In-App-Nachricht klickt. Um zu vermeiden, dass die Erlaubnis für Push-Benachrichtigungen zweimal oder zum falschen Zeitpunkt angefordert wird, sollte ein Entwickler die von ihm implementierte Integration von Push-Benachrichtigungen ändern, um sicherzustellen, dass Ihre In-App-Nachricht die erste Push-Benachrichtigung ist, die Ihre Benutzer sehen.

Ihr Entwickler:in Team sollte die Implementierung von Push-Benachrichtigungen für Ihre App oder Website überprüfen und jeglichen Code, der eine Push-Erlaubnis anfragen würde, manuell entfernen. Zum Beispiel würden Sie Referenzen auf den folgenden Code entfernen:

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

Um Buttons zu Ihrer In-App-Nachricht hinzuzufügen, ziehen Sie zwei **Button-Blöcke** in Ihre Nachricht, die als primäre und sekundäre Buttons in Ihrer In-App-Nachricht fungieren werden. Sie können auch eine Zeile in Ihre Nachricht ziehen und dann die Buttons in die Zeile ziehen, so dass die Buttons in der gleichen horizontalen Zeile stehen (und nicht übereinander gestapelt sind). Wir empfehlen „Benachrichtigungen zulassen“ und „Nicht jetzt“ als Start-Buttons, aber es gibt viele verschiedene Button-Prompts, die Sie zuweisen können.

Nachdem Sie eine Button-Kopie hinzugefügt haben, legen Sie für jeden Button das Verhalten beim Anklicken fest:

- **Button 1:** Legen Sie diesen Button auf „Nachricht schließen“ fest. Dies ist Ihr zweiter Button oder die Option „Nicht jetzt“.
- **Button 2:** Legen Sie diesen Button auf „Push-Berechtigung anfordern“ fest. Dies ist Ihr primärer Button oder die Option „Benachrichtigungen zulassen“.

![In-App-Nachricht-Editor mit zwei Buttons: "Benachrichtigungen zulassen" und "Nicht jetzt".]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Schritt 4: Zeitplan für Zustellung

Um Ihren Push-Primer so einzustellen, dass er zu einem bestimmten Zeitpunkt versendet wird, müssen Sie Ihre In-App-Nachricht als aktionsbasierte Nachricht mit **Angepasstes Event durchführen** als triggernde Aktion planen.

Auch wenn der ideale Zeitpunkt variiert, empfiehlt Braze, zu warten, bis ein Benutzer eine [hochwertige Aktion](https://www.braze.com/resources/videos/mapping-high-value-actions) durchgeführt hat, die anzeigt, dass er einen Nutzen in Ihrer App oder Website sieht, oder wenn es ein zwingendes Bedürfnis gibt, das durch Push-Benachrichtigungen erfüllt werden kann (z. B. nachdem der Benutzer eine Bestellung aufgegeben hat und Sie ihm Informationen zur Sendungsverfolgung anbieten möchten). Auf diese Weise ist die Aufforderung nicht nur für Ihre Marke, sondern auch für den Kunden von Vorteil.

![Aktionsbasierte Zustellung an Nutzer:innen, die das angepasste Event "Zur Beobachtungsliste hinzufügen" ausgeführt haben.]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Schritt 5: Zielnutzer:innen

Das Ziel einer Push-Primer Kampagne ist es, Nutzer:innen auf Geräten, für die sie noch keine Push-Berechtigungen erteilt haben, aufzufordern. Das können erstmalige Nutzer:innen oder bestehende Nutzer:innen sein, die ein neues Gerät erhalten oder Ihre Anwendung neu installieren. Um Ihre Push-Primer-Kampagne richtig zu targetieren, fügen Sie einen Filter hinzu, bei dem `Foreground Push Enabled For App is false`. Dieser Filter identifiziert einzelne App-Installationen, die noch nicht für Push-Benachrichtigungen im Vordergrund opt-in sind.

{% alert important %}
Die Verwendung eines Filters auf Benutzerebene wie `Push Subscription Status is not Opted In` schließt Nutzer:innen aus, die bereits auf einem anderen Gerät ein Opt-in haben, und verhindert, dass sie die Aufforderung auf ihrem neuen Gerät erhalten.
{% endalert %}

Darüber hinaus können Sie entscheiden, welche zusätzlichen Segmente Sie für sinnvoll halten. So könnten Sie beispielsweise Nutzer ansprechen, die einen zweiten Kauf getätigt haben, Nutzer, die gerade ein Konto erstellt haben, um Mitglied zu werden, oder sogar Nutzer, die Ihre App mehr als zweimal pro Woche besuchen. Die gezielte Ansprache von Nutzern in diesen wichtigen Segmenten erhöht die Wahrscheinlichkeit, dass sich die Nutzer für die Push-Funktion entscheiden und diese aktivieren.

## Schritt 6: Konversions-Events

Braze schlägt Standardeinstellungen für Konvertierungen vor, aber vielleicht möchten Sie [Konvertierungsereignisse]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) für Push-Primer einrichten.

