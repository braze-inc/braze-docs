---
nav_title: "Über Push-Benachrichtigungen"
article_title: Über Push-Benachrichtigungen
page_order: 0
page_type: reference
description: "Dieser Referenzartikel gibt einen kurzen Überblick über Push-Benachrichtigungen, stellt Ressourcen für den Einstieg in Push-Nachrichten bereit und weist auf einige Vorschriften hin."
channel:
  - Push

---

# [![Braze Learning Kurs]](https://learning.braze.com/messaging-channels-push) ( [{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-push){: style="float:right;width:120px;border:0;" class="noimgborder"}Über Push-Benachrichtigungen

> Push-Benachrichtigungen eignen sich hervorragend für zeitkritische Handlungsaufforderungen und um Nutzer, die die App schon länger nicht mehr besucht haben, wieder zu aktivieren. Erfolgreiche Push-Kampagnen führen den Nutzer direkt zum Inhalt und demonstrieren den Wert Ihrer Anwendung.

Denken Sie daran, dass die Nutzer sich für Push entscheiden müssen, um Ihre Nachrichten zu erhalten. Es ist also eine gute Idee, Ihren Kunden mit In-App-Nachrichten zu erklären, warum Sie ihnen Push-Benachrichtigungen senden möchten und welchen Nutzen die Aktivierung von Push für sie hat. Dieser Vorgang wird [Push Priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) genannt.

![Beispiel für Push-Nachrichten über Apple Produkte.][1]{: height="400px"}  ![Beispiel für eine Push-Nachricht von Stopwatch auf dem Startbildschirm eines iPhones, die lautet: „Hallo! Dies ist ein iOS Push".][2]{: height="400px"}

Weitere Beispiele für Push-Benachrichtigungen finden Sie in unseren [Fallstudien][8].

## Potenzielle Anwendungsfälle

Push-Benachrichtigungen sind ein hervorragendes Tool, um neue Nutzer:innen zu gewinnen und Kampagnen zur erneuten Interaktion durchzuführen. Hier sind einige Beispiele für gängige Anwendungsfälle von Push-Nachrichten.

| Anwendungsfall | Erklärung |
| -------- | ----------- |
| Erstes Onboarding | Solange Nutzer nicht die ersten Schritte zur Nutzung Ihrer App unternehmen (z. B. ein Konto registrieren), ist ihr Wert stark eingeschränkt. Verwenden Sie Push-Benachrichtigungen, um die Nutzer:innen aufzufordern, diese Schritte abzuschließen, damit sie Ihre App in vollem Umfang nutzen können. |
| Erste Käufe | Nachdem sich die Nutzer:innen mit Ihrer App vertraut gemacht haben, können Sie sie mit Push-Benachrichtigungen zu In-App-Käufern machen. |
| Neue Funktionen | Push-Benachrichtigungen können effektiv sein, wenn es darum geht, desinteressierte Nutzer über neue Funktionen zu informieren, die sie wieder zu Ihrer App locken könnten. |
| Zeitkritische Angebote | Wenn die Uhr für ein Angebot tickt, ist eine Push-Funktion manchmal eine gute Möglichkeit, Ihre Nutzer darüber zu informieren, bevor es abläuft. Diese Nachrichten haben in der Regel einen hohen Dringlichkeitscharakter und sind optimal geeignet, um kürzlich verstorbene Nutzer an Ihre App zu erinnern.<br><br> Nehmen wir an, Ihre App ist ein Spiel und Sie bieten Ihren Nutzern einen Bonus in Form einer Spielwährung, wenn sie das Spiel täglich spielen. Wenn ein Benutzer eine bestimmte Anzahl von Tagen überschritten hat, könnte es sinnvoll sein, ihn darauf hinzuweisen, dass die Serie zu brechen droht. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Informationen zur erneuten Interaktion mit ausgetretenen Nutzer:innen finden Sie auf unserer [Quick Wins][23] Seite zu diesem Thema.

## Voraussetzungen für die Verwendung von Push

Bevor Sie mit Braze Push-Nachrichten erstellen und versenden können, müssen Sie mit Ihren Entwicklern zusammenarbeiten, um Push in Ihre Website oder App zu integrieren. Detaillierte Schritte finden Sie in unseren Integrationsanleitungen für jede Plattform:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Internet]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Vorschriften für Push-Nachrichten

Da es sich bei Push-Nachrichten um eine aufdringliche Art von Nachrichten handelt, die direkt an das Telefon oder den Browser Ihres Kunden gesendet werden, gibt es Richtlinien für den Versand von Push-Nachrichten über Apps und Websites.

### Mobile Push-Vorschriften für Apps

{% alert important %}
Ihre Push-Nachrichten müssen den Richtlinien des Apple App Stores und des Google Play Stores entsprechen, insbesondere in Bezug auf die Verwendung von Push-Nachrichten als Werbung, Spam, Promotions und mehr.
{% endalert %}

|Richtlinien für den Apple App Store|
|---|
|[3.2.2][9] Inakzeptabel: (i) Schaffung einer Schnittstelle für die Anzeige von Apps, Erweiterungen oder Plug-ins von Drittanbietern ähnlich dem App Store oder als Sammlung von allgemeinem Interesse.| 
|[4.5.4][7] Push-Benachrichtigungen dürfen nicht für das Funktionieren der App erforderlich sein und sollten nicht dazu verwendet werden, sensible persönliche oder vertrauliche Informationen zu versenden. Push-Benachrichtigungen sollten nicht für Werbe- oder Direktmarketingzwecke verwendet werden, es sei denn, die Kunden haben sich über eine in der Benutzeroberfläche Ihrer App angezeigte Zustimmungserklärung ausdrücklich für den Erhalt dieser Nachrichten entschieden und Sie bieten in Ihrer App eine Methode an, mit der ein Benutzer den Erhalt solcher Nachrichten ablehnen kann.|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) Sie dürfen keine von der Hardware oder dem Betriebssystem bereitgestellten integrierten Funktionen wie Push-Benachrichtigungen, die Kamera oder das Gyroskop oder Apple-Dienste und -Technologien wie den Zugriff auf Apple Music, iCloud-Speicher oder Screen Time APIs zu Geld machen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Google Play Store Richtlinie|
|---|
|[Unerlaubte Nutzung oder Nachahmung von Systemfunktionen][10] Wir erlauben keine Apps oder Anzeigen, die Systemfunktionen wie Benachrichtigungen oder Warnungen nachahmen oder stören. Benachrichtigungen auf Systemebene dürfen nur für integrierte Funktionen einer App verwendet werden, z. B. eine Fluglinien-App, die Benutzer über Sonderangebote informiert, oder ein Spiel, das Benutzer über Werbeaktionen im Spiel benachrichtigt.|
{: .reset-td-br-1 role="presentation" }

[1]: {% image_buster /assets/img/red-dress.gif %}
[2]: {% image_buster /assets/img/ios_push.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[8]: https://www.braze.com/customers
[7]: https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services
[9]: https://developer.apple.com/app-store/review/guidelines/#unacceptable
[10]: https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories
[23]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
