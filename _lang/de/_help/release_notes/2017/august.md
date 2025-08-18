---
nav_title: August
page_order: 5
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für August 2017."
---

# August 2017

## Update auf Push-Action-Buttons

Wir haben unseren REST API Messaging Endpunkten Unterstützung für [Push-Action-Buttons]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons) hinzugefügt.

## Update auf Liquid Templating

Sie können jetzt [eine Nachricht personalisieren]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/), und zwar auf der Grundlage von:
- Das Gerät, an das es gesendet wurde,
- ID des Geräts,
- Spediteur,
- IDENTIFIER FOR ADVERTISERS (IDFA),
- Modell,
- OS, und
- Plattform

## API-getriggertes Canvas

Sie können jetzt ein [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) über API-Endpunkte (Senden, Zeitplan, Update, Löschen) triggern, die mit den bereits vorhandenen für Kampagnen übereinstimmen, was eine weitere Automatisierung und Optimierung Ihres Marketings zulässt.

## Internet Push-Action-Buttons

Wir haben das Web SDK für Chrome um Unterstützung für Push-Action-Buttons erweitert, die es Ihnen erlaubt, Ihr Engagement zu steigern, indem Sie Ihren Nutzer:innen kontextuelle Auswahlmöglichkeiten bieten, die ihr geschäftiges Leben vereinfachen. Informieren Sie sich über die [besten Praktiken für Push-Benachrichtigungen]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/).

## Neue API Endpunkte

Wir haben neue API Endpunkte eingerichtet: /email/hard_bounces, mit dem Sie Hard Bounces nach E-Mail-Adressen oder in einem bestimmten Datumsbereich abrufen können, und /messages/scheduled_broadcasts, mit dem Sie den nächsten Zeitpunkt abrufen können, zu dem geplante Kampagnen und Canvase mit geplantem Eingang beginnen werden. Diese neuen Endpunkte ermöglichen Ihnen eine weitere Anpassung und Optimierung Ihrer Kampagnen. Erfahren Sie mehr über unsere [API Endpunkte]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api).

## Geofences

Wir haben ein neues Feature, Geoofences, hinzugefügt, das es Ihnen erlaubt, Nachrichten in Realtime zu triggern, wenn Kunden ein bestimmtes geografisches Gebiet betreten oder verlassen, und so eine personalisierte, relevante Kommunikation mit Ihren Kunden zu ermöglichen. Erfahren Sie mehr über [Standort Marketing]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/).

## Update für den E-Mail Editor

Wir haben unseren neuen E-Mail-Editor mit einer dynamischen Autovervollständigung ausgestattet, so dass Sie bei der Verwendung von Liquid nun automatisch die tatsächlich angepassten Attribute und Events Ihrer Kund:in ausfüllen können, was Ihnen das Leben leichter macht. Erfahren Sie mehr über die [besten Praktiken bei E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices).

## Update auf Datumsfilter

Wir haben einen "Nie"-Datum-Filter hinzugefügt, mit dem Sie gezielt Kunden ansprechen können, die noch nie eine Ihrer Nachrichten erhalten oder mit ihnen interagiert haben. So können Sie eine saubere Kunden-Liste führen und die Zustellbarkeit von E-Mails sicherstellen. Erfahren Sie mehr über [Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters).

## Update auf Canvas

Wir haben am oberen Rand jeder Canvas-Variante Prozentzahlen hinzugefügt, damit Sie auf einen Blick sehen können, welche Varianten eine bessere Performance aufweisen. Erfahren Sie mehr über [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

## Canvas mit intelligenter Auswahl

Canvas verfügt jetzt über eine intelligente Auswahl, die es Ihnen erlaubt, Ihre Canvase mit größerer Effizienz zu testen. Erfahren Sie mehr über unsere [Intelligence Suite]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

## Update für die Anzeige von Namen in E-Mails

Wir haben die Unterstützung von UTF-8-Sonderzeichen in E-Mail-Anzeigenamen hinzugefügt, so dass Sie noch personalisiertere E-Mails für Ihre Kunden erstellen können. Erfahren Sie mehr über die [besten Praktiken bei E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices).

## Engagement-Berichte CSV-Aggregation

Jetzt können Sie konsolidierte Daten für jede Kampagne und jedes Canvas in zwei separaten Dateien erhalten, unabhängig davon, wie viele Kampagnen oder Canvase ausgewählt sind. So haben Sie alle Daten, die Sie benötigen, immer zur Hand. Erfahren Sie mehr über [Engagement-Berichte]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/).

> Wie in unseren [Versionshinweisen vom September 2017]({{site.baseurl}}/help/release_notes/2017/september/) erwähnt, können Sie jetzt Daten aus einem bestimmten Zeitraum aggregieren und Exporte für eine wiederkehrende Basis planen.


