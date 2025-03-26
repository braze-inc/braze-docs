---
nav_title: Juli
page_order: 6
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Juli 2016."
---

# Juli 2016

## Filterung des Fehlerprotokolls der Entwicklerkonsole nach Fehlertyp

Dieses Upgrade erleichtert Ihnen die Verwendung des Message Error Logs in der Developer Console, um Probleme mit ihren Braze-Integrationen zu beheben. Dies ist eine Aktualisierung der Benutzerfreundlichkeit, die es Ihnen ermöglicht, das Meldungs-Fehlerprotokoll nach Typ zu filtern, und die das Auffinden und Identifizieren bestimmter Integrationsprobleme erheblich erleichtert.

## Zeitstempel für den letzten gesendeten Push zur Deinstallationsverfolgung hinzugefügt

Braze erkennt Deinstallationen, indem es einen stillen Push an die Apps eines Kunden sendet, um zu sehen, welche Geräte reagieren. Diese Funktion fügt einen unauffälligen Zeitstempel hinzu, der anzeigt, wann die Deinstallationsüberwachung zuletzt ausgeführt wurde. Diesen Zeitstempel finden Sie auf Ihrer Einstellungsseite, auf der die Deinstallationsverfolgung konfiguriert ist. Erfahren Sie mehr über die [Deinstallationsverfolgung]({{site.baseurl}}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking).

![Kontrollkästchen Tracking deinstallieren][6]

## Verbesserungen der Webhook-Tests hinzugefügt

Sie können jetzt eine Live-Webhook-Nachricht von Braze senden, bevor Sie eine Kampagne in Betrieb nehmen. Durch das Versenden einer Testnachricht können Sie überprüfen, ob Ihre Nachrichten und Serverendpunkte in einer sicheren Sandbox-Umgebung richtig konfiguriert wurden. Erfahren Sie mehr über [Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook).

## Der CSV-Export für Kampagnenempfänger wurde um die Variation der empfangenen Nachricht erweitert.

Wir haben dem CSV-Export für Kampagnenempfänger eine Spalte hinzugefügt, die die erhaltene Nachrichtenvariante angibt. Erfahren Sie mehr über den [Export von Daten]({{site.baseurl}}/user_guide/data_and_analytics/exporting_dashboard_data/#exporting-dashboard-data) aus Braze.

## Ungefähres Limit für die Anzahl der Impressionen

Sobald eine In-App-Nachricht eine bestimmte Anzahl von Impressionen erhalten hat, erlaubt Braze seinen Nutzern nicht mehr, die Nachricht zu erhalten. Erfahren Sie mehr über das Festlegen von ungefähren [Grenzen für Impressionen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap).

![IAM Abdruckkappe][11]

[6]: {% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %}
[11]: {% image_buster /assets/img_archive/approx_limit_for_IAM.png %}
