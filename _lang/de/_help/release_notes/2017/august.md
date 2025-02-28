---
nav_title: August
page_order: 5
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für August 2017."
---

# August 2017

## Aktualisieren, um Aktionstasten zu drücken

Wir haben unsere REST-API-Nachrichtenendpunkte um Unterstützung für [Push-Aktionsschaltflächen][70] erweitert.

## Update für Liquid Templating

Sie können jetzt [eine Nachricht][69] auf der Grundlage von:
- Das Gerät, an das sie gesendet wurde,
- Geräte-ID,
- Spediteur,
- IDFA,
- Modell,
- OS, und
- Plattform

## API-gesteuertes Canvas

Sie können jetzt einen [Canvas][68] über API-Endpunkte (Senden, Planen, Aktualisieren, Löschen) auslösen, die mit den bereits vorhandenen für Kampagnen übereinstimmen. So können Sie Ihr Marketing weiter automatisieren und optimieren.

## Web-Push-Aktionsschaltflächen

Wir haben das Web-SDK für Chrome um Unterstützung für Push-Action-Buttons erweitert. So können Sie das Engagement Ihrer Nutzer erhöhen, indem Sie ihnen kontextbezogene Auswahlmöglichkeiten bieten, die ihr geschäftiges Leben vereinfachen. Informieren Sie sich über die [besten Praktiken für Push-Benachrichtigungen][66].

## Neue API-Endpunkte

Wir haben neue API-Endpunkte eingerichtet: /email/hard_bounces, mit dem Sie Hard Bounces nach E-Mail-Adresse oder in einem bestimmten Datumsbereich abrufen können, und /messages/scheduled_broadcasts, mit dem Sie den nächsten Zeitpunkt für geplante Kampagnen und Canvases mit geplantem Eintrag abrufen können. Diese neuen Endpunkte ermöglichen Ihnen eine weitere Anpassung und Optimierung Ihrer Kampagnen. Erfahren Sie mehr über unsere [API-Endpunkte][65].

## Geofences

Wir haben eine neue Funktion, Geofences, hinzugefügt, mit der Sie Nachrichten in Echtzeit auslösen können, wenn Kunden bestimmte geografische Gebiete betreten oder verlassen, was eine personalisierte, relevante Kommunikation mit Ihren Kunden ermöglicht. Erfahren Sie mehr über [Standortmarketing][64].

## Update für E-Mail-Editor

Wir haben unseren neuen E-Mail-Editor mit einer dynamischen Autovervollständigung ausgestattet, so dass Sie jetzt bei der Verwendung von Liquid die tatsächlichen benutzerdefinierten Attribute und Ereignisse Ihrer Kunden automatisch vervollständigen können, was Ihnen das Leben erleichtert. Erfahren Sie mehr über bewährte E-Mail-Verfahren in [Academy][63].

## Update auf Datumsfilter

Wir haben einen "Nie"-Datumsfilter hinzugefügt, mit dem Sie Kunden ansprechen können, die nie eine Ihrer Nachrichten erhalten oder mit ihnen interagiert haben. So können Sie saubere Kundenlisten führen und die Zustellbarkeit Ihrer E-Mails sicherstellen. Erfahren Sie mehr über [Filter][62].

## Update auf Canvas

Wir haben am oberen Rand jeder Canvas-Variante Prozentsätze hinzugefügt, so dass Sie jetzt auf einen Blick sehen können, welche Varianten besser abschneiden. Erfahren Sie mehr über [Canvas][61].

## Leinwand mit intelligenter Auswahl

Canvas verfügt jetzt über eine intelligente Auswahl, mit der Sie Ihre Leinwände effizienter testen können. Erfahren Sie mehr über unsere [Intelligence Suite][60].

## Aktualisierung der E-Mail-Anzeigenamen

Wir haben die Unterstützung von UTF-8-Sonderzeichen in E-Mail-Anzeigenamen hinzugefügt, so dass Sie noch persönlichere E-Mails für Ihre Kunden erstellen können. Erfahren Sie mehr über [bewährte E-Mail-Verfahren][67].

## Engagement-Berichte CSV-Aggregation

Jetzt können Sie konsolidierte Daten für jede Kampagne und jedes Canvas in zwei separaten Dateien erhalten, unabhängig davon, wie viele Kampagnen oder Canvases ausgewählt sind. So haben Sie alle Daten, die Sie brauchen, wann Sie sie brauchen. Erfahren Sie mehr über [Engagement Reports][59].

> Wie in unseren [Versionshinweisen vom September 2017]({{site.baseurl}}/help/release_notes/2017/september/) erwähnt, können Sie jetzt Daten aus einem bestimmten Zeitraum aggregieren und Exporte für eine wiederkehrende Ausführung planen.


[59]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/
[60]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[61]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters
[63]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[64]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/
[65]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[66]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[67]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[68]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[69]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[70]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
