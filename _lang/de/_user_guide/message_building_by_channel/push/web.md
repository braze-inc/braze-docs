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

Web-Push ist eine weitere großartige Möglichkeit, mit den Nutzer:innen Ihrer Webanwendung zu interagieren. Kund:innen, die Ihre Website über [unterstützte Browser](#supported-browsers) besuchen, können sich für den Empfang von Web-Push-Benachrichtigungen Ihrer Webanwendung entscheiden – unabhängig davon, ob die Webseite geladen ist oder nicht.

## Übersicht

Web-Push-Benachrichtigungen liefern dringende, umsetzbare Updates, die zu schnellen Konversionen führen. Mit Web-Push können Sie:

- Nachrichten genau dann triggern, wenn sich wichtige Daten ändern, z. B. bei einem Preisrückgang
- Personen mit eindeutigen Aktions-Buttons zurück auf Ihre Website leiten
- Ihren Push mit Produkt- und Kundeninformationen personalisieren, damit Ihre Nachricht relevant ist

Web-Push funktioniert genauso wie Push-Benachrichtigungen von Apps auf Ihrem Telefon. Weitere Informationen zum Erstellen einer Web-Push-Benachrichtigung finden Sie unter [Push-Benachrichtigung erstellen]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).

![Beispiel für Web-Push mit der gleichen Push-Nachricht, die auf einem Laptop und einem Telefon angezeigt wird.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Potenzielle Anwendungsfälle

Hier sind einige Beispiele für gängige Anwendungsfälle von Web-Push-Nachrichten.

| Anwendungsfall | Beschreibung |
| --- | --- | 
| Kostenlose Demo | Ermutigen Sie neue Besucher:innen auf Ihrer Website, sich für eine kostenlose Demo zu registrieren. Indem Sie Nutzer:innen die Möglichkeit geben, zu erfahren, was Sie besonders macht, erhöhen Sie die Wahrscheinlichkeit, dass sie zu zahlenden Kund:innen werden. |
| App herunterladen | Leiten Sie Internet-Nutzer:innen zu Ihrer mobilen App, damit sie noch mehr Nutzen aus Ihren Produkten ziehen können. Nutzen Sie die Personalisierung, um die Vorteile der App auf Grundlage des aktuellen Nutzungsverhaltens hervorzuheben. |
| Rabatte und Aktionen | Steigern Sie das Bewusstsein Ihrer Kund:innen für zeitkritische Events und Aktionen. Versenden Sie Nachrichten über mehrere Kanäle, einschließlich Web-Push, um die Aufmerksamkeit für die Aktionen Ihrer Marke zu erhöhen. |
| Abgebrochener Einkauf | Senden Sie automatische Erinnerungen an Nutzer:innen, die ihre Transaktionen noch nicht abgeschlossen haben, um sie zurück in den Bezahlvorgang zu bringen. <br><br>Eine von Braze durchgeführte Studie hat ergeben, dass Web-Push 53 % effektiver ist als E-Mail und 23 % wirkungsvoller als mobiler Push, wenn es darum geht, Empfänger:innen dazu zu bringen, zurückzukehren und einen Kauf abzuschließen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Voraussetzungen für die Verwendung von Web-Push

Bevor Sie mit Braze Push-Nachrichten erstellen und versenden können, müssen Sie mit Ihren Entwickler:innen zusammenarbeiten, um Push in Ihre Website zu integrieren. Detaillierte Schritte finden Sie in unserer [Anleitung zur Integration von Web-Push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

### Push-Erlaubnis

Jede Marke kann Web-Push-Benachrichtigungen in ihre Website integrieren und nutzen. Die Benachrichtigungen können sowohl aktuelle als auch frühere Webbesucher:innen erreichen, solange diese einen Webbrowser geöffnet haben. Allerdings müssen die Besucher:innen [dem Erhalt von Benachrichtigungen zustimmen]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission) – genau wie bei herkömmlichen Push-Benachrichtigungen für mobile Apps.

{% alert tip %}
Ziehen Sie eine In-Browser-Nachricht in Betracht, um Nutzer:innen zum Opt-in für Web-Push zu bewegen – auch bekannt als [Push-Primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
{% endalert %}

## Unterstützte Browser

Die folgenden Browser unterstützen Web-Push-Benachrichtigungen.

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

- Chrome (und Chrome für Android-Mobilgeräte)
- Safari (Version 16 oder neuer)
- Firefox (und Firefox für Android-Mobilgeräte)
- Opera
- Edge

Weitere Informationen zu den Push-Protokollstandards und der Browserunterstützung finden Sie in den für Ihren Browser relevanten Ressourcen:

- [Safari (Desktop)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (mobil)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)