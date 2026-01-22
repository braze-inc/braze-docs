---
nav_title: "Web-Push"
article_title: Web-Push-Benachrichtigungen
page_order: 8.5
page_type: reference
description: "Diese Seite behandelt kurz Web-Push-Benachrichtigungen und verweist auf die notwendigen Schritte zu deren Erstellung."
platform: Web
channel:
  - push

---

# Web-Push

> Erfahren Sie mehr über Web-Push-Benachrichtigungen bei Braze und finden Sie Ressourcen für die Erstellung Ihrer eigenen.

Web-Push ist eine weitere großartige Möglichkeit, mit den Nutzer:innen Ihrer Webanwendung zu interagieren. Kunden, die Ihre Website von [unterstützten Browsern](#supported-browsers) aus besuchen, können sich dafür entscheiden, Web Push von Ihrer Webanwendung zu erhalten, unabhängig davon, ob die Webseite geladen ist oder nicht.

## Übersicht

Web-Push-Benachrichtigungen liefern dringende, umsetzbare Updates, die zu schnellen Konversionen führen. Das können Sie mit Web-Push tun:

- Lösen Sie Nachrichten aus, wenn sich wichtige Daten ändern, z. B. ein Preisrückgang.
- Bringen Sie Besucher mit einfachen Aktions-Buttons zurück auf Ihre Website
- Passen Sie Ihren Push mit Produkt- und Kundeninformationen an, damit Ihre Nachricht relevant ist.

Web-Push funktioniert genauso wie die Push-Benachrichtigungen von Apps auf Ihrem Telefon. Weitere Informationen zum Verfassen einer Web-Push-Nachricht finden Sie unter [Erstellen einer Push-Benachrichtigung]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).

![Web-Push-Beispiel mit der gleichen Push Nachricht, die auf einem Laptop und einem Telefon angezeigt wird.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Potenzielle Anwendungsfälle

Hier sind einige Beispiele für gängige Anwendungsfälle von Web-Push-Nachrichten.

| Anwendungsfall | Beschreibung |
| --- | --- | 
| Kostenloser Test | Ermutigen Sie neue Besucher auf Ihrer Website, sich für kostenlose Testversionen zu registrieren. Indem Sie den Nutzern die Möglichkeit geben, zu erfahren, was Sie besonders macht, erhöhen Sie die Wahrscheinlichkeit, dass sie zu zahlenden Kunden werden. |
| App herunterladen | Ziehen Sie Nutzer auf Ihre mobile App, damit sie einen noch größeren Nutzen aus Ihren Produkten ziehen können. Nutzen Sie die Personalisierung, um die Vorteile der App auf der Grundlage ihres aktuellen Nutzungsverhaltens hervorzuheben. |
| Rabatte und Verkäufe | Weisen Sie Ihre Kunden auf zeitkritische Events und Aktionen hin. Nachrichten über mehrere Kanäle einschließlich Web-Push um die Aufmerksamkeit für die Aktionen Ihrer Marke zu erhöhen. |
| Warenkorb-Abbruch | Senden Sie automatische Erinnerungen an Benutzer, die ihre Transaktionen noch nicht abgeschlossen haben, um sie wieder in den Kassenfluss zu bringen. <br><br>Eine von Braze durchgeführte Studie hat ergeben, dass Web-Push-Kampagnen 53 % effektiver sind als E-Mail-Kampagnen und 23 % effektiver als mobile Push-Kampagnen, wenn es darum geht, die Empfänger dazu zu bringen, wiederzukommen und einen Kauf abzuschließen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Voraussetzungen für die Verwendung von Web Push

Bevor Sie mit Braze Push-Nachrichten erstellen und versenden können, müssen Sie mit Ihren Entwicklern zusammenarbeiten, um Push in Ihre Website zu integrieren. Detaillierte Schritte finden Sie in unserer [Anleitung zur Integration von Web-Push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

### Push-Erlaubnis

Jede Marke kann Web-Push-Benachrichtigungen in ihre Website integrieren und nutzen. Die Benachrichtigungen können sowohl aktuelle als auch frühere Webbesucher erreichen, solange diese einen Webbrowser geöffnet haben. Allerdings müssen die Besucher [dem Erhalt von Benachrichtigungen zustimmen - genau]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission)wie bei herkömmlichen Push-Benachrichtigungen für mobile Apps.

{% alert tip %}
Ziehen Sie eine In-Browser-Nachricht in Betracht, um Nutzer zum Opt-in für Web-Push zu bewegen, auch bekannt als [Push-Primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
{% endalert %}

## Unterstützte Browser

Die folgenden Browser unterstützen Web-Push-Benachrichtigungen. Private Browsing-Fenster unterstützen jedoch derzeit keinen Web-Push.

- Chrome (und Chrome für Android Mobil)
- Safari
- Firefox (und Firefox für Android Mobile)
- Opera
- Edge

Weitere Informationen zu den Push-Protokollstandards und der Browserunterstützung finden Sie in den für Ihren Browser relevanten Ressourcen:

- [Safari (Desktop)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (mobil)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)


