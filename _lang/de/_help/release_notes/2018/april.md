---
nav_title: April
page_order: 9
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für April 2018."
---
# April 2018

## Webhooks-Update auf dem Weg

Im Mai wird Braze eine Sicherheitsinitiative für Webhook-Umleitungen einführen. Künftig kann der Webhook-Absender diese Weiterleitungen nicht mehr verfolgen. Stattdessen werden Weiterleitungen als Fehler behandelt, um unendliche Weiterleitungsschleifen zu vermeiden. Braze geht nicht davon aus, dass dies irgendjemanden betrifft, aber wenn Sie Webhooks haben, die umleiten, empfehlen wir Ihnen, diese Kampagne zu überprüfen und zu bearbeiten.

## CSV-Speicher erhöht

Braze hat den CSV X-Filter aktualisiert, so dass er nun die 100 letzten CSVs, in denen ein Benutzer aktualisiert wurde, enthält und nicht mehr nur die letzten 10.

## Standardmäßig eingeschaltetes Tracking für Android-Apps deinstallieren

Die Funktion [zur Deinstallationsverfolgung][94] ist für alle neuen Android-Apps standardmäßig aktiviert. Alle bestehenden Android-Apps, bei denen die Deinstallationsverfolgung ausgeschaltet ist, werden jetzt auf "ein" gesetzt. Die Android-Deinstallationsverfolgung sendet keine Push-Nachrichten mehr an das Gerät, und es sind keine weiteren Updates oder Aktionen Ihrerseits erforderlich.

## Aktualisierte und verbesserte Suchfunktionen

Braze hat Tagging und eine bessere Suchfunktionalität hinzugefügt, um Ihnen die Verwaltung umfangreicher Braze-Implementierungen zu erleichtern, während Sie nach [benutzerdefinierten Ereignissen und Attributen][92], Vorlagen und mehr suchen.

## Push-Storys

[Erstellen Sie Benachrichtigungen][95] mit mehreren Seiten, einem Bild, Klickverhalten und einem optionalen Titel und Untertitel. Erstellen Sie einfach eine Push-Nachricht und wählen Sie **Push Story** aus der Dropdown-Liste.

Beachten Sie, dass Sie auf die neueste Version von Android (Version 2.2.0+) und iOS (Version 3.2.0+) aktualisieren müssen, um diese Funktion zu nutzen.


## Posteingang Vision

Sie können jetzt [eine Vorschau Ihrer E-Mails][96] auf der Grundlage der Plattform Ihres Kunden [anzeigen][96], entweder über eine Übersichtsseite mit Miniaturansichten oder eine Listenansicht, die einen großen Screenshot und eine genauere Analyse von Problemen mit der HTML-Darstellung für jeden Kunden enthält. Wenden Sie sich für weitere Informationen an Ihren Kundenbetreuer oder Account Manager.


[92]: {{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#custom-event-and-attribute-management
[94]: {{site.baseurl}}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking-for-campaigns
[95]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_stories/#push-stories
[96]: {{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision
