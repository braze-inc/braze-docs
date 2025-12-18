---
nav_title: Push
article_title: Push
page_order: 4
layout: dev_guide
guide_top_header: "Push"
guide_top_text: "Push-Benachrichtigungen sind eine bewährte Methode, um zeitkritische Handlungsaufforderungen über das Handy oder das Internet zu versenden und Nutzer:innen, die die App schon länger nicht mehr besucht haben, erneut zu engagieren. Sie führen den Nutzer:innen direkt zum Inhalt und demonstrieren den Wert Ihrer Anwendung. Push-Benachrichtigungen sind nützlich, um Nutzer:innen an einen bestimmten Ort zu bringen, aber Sie sollten sie mit Bedacht einsetzen. <br><br> Lesen Sie einen der folgenden Artikel oder sehen Sie sich unseren [Push Braze Lernkurs] (https://learning.braze.com/messaging-channels-push) an, um zu erfahren, an wen Sie einen Push senden können, wie Sie ihn senden können und welche erweiterten Push-Funktionen Braze bietet. Beispiele für Push-Benachrichtigungen finden Sie in unseren [Kunden-Storys](https://www.braze.com/customers)."
description: "Auf dieser Landing-Page finden Sie Push-Nachrichten. Hier finden Sie Artikel über Push-Typen, Push-Registrierung, Push-Enablement, Push-Primer, Push-Berichte und mehr."
channel:
  - push

guide_featured_title: "Beliebte Artikel"
guide_featured_list:
- name: Push-Typen
  link: /docs/user_guide/message_building_by_channel/push/types/
  image: /assets/img/braze_icons/list.svg
- name: Push-Registrierung
  link: /docs/user_guide/message_building_by_channel/push/push_registration/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Push-Aktivierung und Abonnement
  link: /docs/user_guide/message_building_by_channel/push/users_and_subscriptions/
  image: /assets/img/braze_icons/users-01.svg
- name: Erstellen einer Push Nachricht
  link: /docs/user_guide/message_building_by_channel/push/creating_a_push_message/
  image: /assets/img/braze_icons/edit-05.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: Erweiterte Optionen
  link: /docs/user_guide/message_building_by_channel/push/advanced_push_options/
  image: /assets/img/braze_icons/settings-01.svg
- name: Push Primer
  link: /docs/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
  image: /assets/img/braze_icons/phone-02.svg
- name: Berichterstattung
  link: /docs/user_guide/message_building_by_channel/push/push_reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Android-Optionen
  link: /docs/user_guide/message_building_by_channel/push/android/
  image: /assets/img/braze_icons/android.svg
- name: iOS Optionen
  link: /docs/user_guide/message_building_by_channel/push/ios/
  image: /assets/img/braze_icons/apple.svg
- name: Web-Push
  link: /docs/user_guide/message_building_by_channel/push/web/
  image: /assets/img/braze_icons/monitor-01.svg
- name: Bewährte Praktiken
  link: /docs/user_guide/message_building_by_channel/push/best_practices/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Lokale in Nachrichten
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: Allgemeine Push-Fehlermeldungen
  link: /docs/user_guide/message_building_by_channel/push/push_error_codes/
  image: /assets/img/braze_icons/alert-triangle.svg
- name: Fehlersuche
  link: /docs/user_guide/message_building_by_channel/push/troubleshooting/
  image: /assets/img/braze_icons/annotation-question.svg
- name: Häufig gestellte Fragen
  link: /docs/user_guide/message_building_by_channel/push/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![Braze Lernkurse]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"} Anwendungsfälle

![Beispiel für Push-Nachrichten über Apple Produkte.]({% image_buster /assets/img/red-dress.gif %}){: height="400px"} ![Beispiel für eine Push Nachricht von Stopwatch auf dem Startbildschirm eines iPhones, die lautet: „Hallo! Dies ist ein iOS Push".]({% image_buster /assets/img/ios_push.png %}){: height="400px"}

Push-Benachrichtigungen sind ein hervorragendes Tool, um neue Nutzer:innen zu gewinnen und Kampagnen zur erneuten Interaktion durchzuführen. Hier sind einige Beispiele für gängige Anwendungsfälle von Push-Nachrichten.

| Anwendungsfall | Erklärung |
| -------- | ----------- |
| Erstes Onboarding | Solange Nutzer nicht die ersten Schritte zur Nutzung Ihrer App unternehmen (z. B. ein Konto registrieren), ist ihr Wert stark eingeschränkt. Verwenden Sie Push-Benachrichtigungen, um die Nutzer:innen aufzufordern, diese Schritte abzuschließen, damit sie Ihre App in vollem Umfang nutzen können. |
| Erste Käufe | Nachdem sich die Nutzer:innen mit Ihrer App vertraut gemacht haben, können Sie sie mit Push-Benachrichtigungen zu In-App-Käufern machen. |
| Neue Funktionen | Push-Benachrichtigungen können effektiv sein, wenn es darum geht, desinteressierte Nutzer über neue Funktionen zu informieren, die sie wieder zu Ihrer App locken könnten. |
| Zeitkritische Angebote | Wenn die Uhr für ein Angebot tickt, ist eine Push-Funktion manchmal eine gute Möglichkeit, Ihre Nutzer darüber zu informieren, bevor es abläuft. Diese Nachrichten haben in der Regel einen hohen Dringlichkeitscharakter und sind optimal geeignet, um kürzlich verstorbene Nutzer an Ihre App zu erinnern.<br><br> Nehmen wir an, Ihre App ist ein Spiel und Sie bieten Ihren Nutzern einen Bonus in Form einer Spielwährung, wenn sie das Spiel täglich spielen. Wenn ein Benutzer eine bestimmte Anzahl von Tagen überschritten hat, könnte es sinnvoll sein, ihn darauf hinzuweisen, dass die Serie zu brechen droht. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Informationen zur erneuten Interaktion mit ausgetretenen Nutzer:innen finden Sie auf unserer Seite [Quick Wins]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users).

## Voraussetzungen für die Verwendung von Push

Bevor Sie mit Braze Push-Nachrichten erstellen und versenden können, müssen Sie mit Ihren Entwicklern zusammenarbeiten, um Push in Ihre Website oder App zu integrieren. Detaillierte Schritte finden Sie in unseren Integrationsanleitungen für jede Plattform:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Internet]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Push-Priming

Denken Sie daran, dass die Nutzer sich für Push entscheiden müssen, um Ihre Nachrichten zu erhalten. Es ist also eine gute Idee, Ihren Kunden mit In-App-Nachrichten zu erklären, warum Sie ihnen Push-Benachrichtigungen senden möchten und welchen Nutzen die Aktivierung von Push für sie hat. Dieser Vorgang wird [Push Priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) genannt.

## Vorschriften für Push-Nachrichten

Da es sich bei Push-Nachrichten um eine aufdringliche Art von Messaging handelt, die direkt an das Telefon oder den Browser Ihres Kunden geht, gibt es Richtlinien für das Versenden von Push-Nachrichten über Apps und Websites.

### Mobile Push-Vorschriften für Apps

{% alert important %}
Ihre Push-Nachrichten müssen den Richtlinien des Apple App Stores und des Google Play Stores entsprechen, insbesondere in Bezug auf die Verwendung von Push-Nachrichten als Werbung, Spam, Promotions und mehr.
{% endalert %}

|Richtlinien für den Apple App Store|
|---|
|[3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) Inakzeptabel: (i) Schaffung einer Schnittstelle für die Anzeige von Apps, Erweiterungen oder Plug-ins von Drittanbietern ähnlich dem App Store oder als Sammlung von allgemeinem Interesse.| 
|[4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) Push-Benachrichtigungen dürfen für das Funktionieren der App nicht erforderlich sein und sollten nicht dazu verwendet werden, sensible persönliche oder vertrauliche Informationen zu versenden. Push-Benachrichtigungen sollten nicht für Werbe- oder Direktmarketingzwecke verwendet werden, es sei denn, die Kunden haben sich über eine in der Benutzeroberfläche Ihrer App angezeigte Zustimmungserklärung ausdrücklich für den Erhalt dieser Nachrichten entschieden und Sie bieten in Ihrer App eine Methode an, mit der ein Benutzer den Erhalt solcher Nachrichten ablehnen kann.|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) Sie dürfen keine von der Hardware oder dem Betriebssystem bereitgestellten integrierten Funktionen wie Push-Benachrichtigungen, die Kamera oder das Gyroskop oder Apple-Dienste und -Technologien wie den Zugriff auf Apple Music, iCloud-Speicher oder Screen Time APIs zu Geld machen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Google Play Store Richtlinie|
|---|
|[Unerlaubte Nutzung oder Nachahmung von Systemfunktionen](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) Wir lassen keine Apps oder Anzeigen zu, die Systemfunktionen wie Benachrichtigungen oder Warnungen imitieren oder stören. Benachrichtigungen auf Systemebene dürfen nur für integrierte Funktionen einer App verwendet werden, z. B. eine Fluglinien-App, die Benutzer über Sonderangebote informiert, oder ein Spiel, das Benutzer über Werbeaktionen im Spiel benachrichtigt.|
{: .reset-td-br-1 role="presentation" }
